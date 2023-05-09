import weaviate
import json

with open('./keys/openai_key.txt', 'r') as f:
    api_tkn = f.read().strip()

client = weaviate.Client(
    url="http://localhost:8080/",
    # auth_client_secret=weaviate.auth.AuthApiKey(api_key="<YOUR-WEAVIATE-API-KEY>"),
    additional_headers={
        "X-OpenAI-Api-Key": api_tkn,
    },
)

# Delete existing schema (if necessary - THIS WILL ALSO DELETE ALL OF YOUR DATA)
client.schema.delete_all()

# Fetch & inspect schema (should be empty)
schema = client.schema.get()
print(json.dumps(schema, indent=4))

# ===== add schema ===== 
# https://weaviate.io/developers/weaviate/tutorials/schema
# see the above link for fully fleshing out this schema.
class_obj = {
    "class": "Question",
    "vectorizer": "text2vec-openai"  # Or "text2vec-cohere" or "text2vec-huggingface"
}

client.schema.create_class(class_obj)

# ===== import data ===== 
# Load data from GitHub
import requests
url = 'https://raw.githubusercontent.com/weaviate/weaviate-examples/main/jeopardy_small_dataset/jeopardy_tiny.json'
resp = requests.get(url)
data = json.loads(resp.text)

# Configure a batch process
with client.batch as batch:
    batch.batch_size=100
    # Batch import all Questions
    for i, d in enumerate(data):
        print(f"importing question: {i+1}")

        properties = {
            "answer": d["Answer"],
            "question": d["Question"],
            "category": d["Category"],
        }

        client.batch.add_data_object(properties, "Question")

client.data_object.get()
