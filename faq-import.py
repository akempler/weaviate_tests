import weaviate
import json
import requests

with open('./keys/openai_key.txt', 'r') as f:
    api_tkn = f.read().strip()

client = weaviate.Client(
    url="http://localhost:8080/",
    # auth_client_secret=weaviate.auth.AuthApiKey(api_key="<YOUR-WEAVIATE-API-KEY>"),
    additional_headers={
        "X-OpenAI-Api-Key": api_tkn,
    },
)

schema = client.schema.get()
# print(json.dumps(schema, indent=4))

# ===== import data ===== 
# Load data from GitHub
url = 'https://raw.githubusercontent.com/akempler/sample_data/main/jury_faqs.json'
resp = requests.get(url)
data = json.loads(resp.text)
print(json.dumps(data, indent=4))

# Configure a batch process
with client.batch as batch:
    batch.batch_size=100
    # Batch import all Faqs
    for i, d in enumerate(data):
        print(f"importing faq: {i+1}")

        properties = {
            "category": d["category"],
            "answer": d["answer"],
            "question": d["question"],
        }

        client.batch.add_data_object(properties, "Question")

client.data_object.get()
