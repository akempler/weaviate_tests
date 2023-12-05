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
    "description": "Faqs for querying",
    "properties": [
        {
            "dataType": ["text"],
            "description": "The title/question of the faq",
            "name": "title",
        },
        {
            "dataType": ["text"],
            "description": "The text/answer of the faq",
            "name": "textVector",
        },
        {
            "dataType": ["text"],
            "description": "The faq category",
            "name": "category",
        }
    ],
    "vectorizer": "text2vec-transformers",
}

client.schema.create_class(class_obj)

schema = client.schema.get()
print(json.dumps(schema, indent=4))
