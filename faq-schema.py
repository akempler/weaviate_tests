import weaviate
import json

with open('./keys/openai_key.txt', 'r') as f:
    api_tkn = f.read().strip()

client = weaviate.Client(
    url="http://localhost:8080/",
)

# ===== add schema ===== 
class_obj = {
    "class": "Faq",
    "description": "Information from a Jeopardy! question",  # description of the class
    "properties": [
        {
            "dataType": ["text"],
            "description": "The category",
            "name": "category",
        },
        {
            "dataType": ["text"],
            "description": "The question",
            "name": "question",
        },
        {
            "dataType": ["text"],
            "description": "The answer",
            "name": "answer",
        }
    ],
    "vectorizer": "text2vec-openai",
}

client.schema.create_class(class_obj)

schema = client.schema.get()
print(json.dumps(schema, indent=4))

