import weaviate
import json

with open('./keys/openai_key.txt', 'r') as f:
    api_tkn = f.read().strip()

client = weaviate.Client(
    url="http://localhost:8080/",
)

# ===== add schema ===== 
class_obj = {
    "class": "JudicalDocument",
    "description": "Documents for querying",  # description of the class
    "properties": [
        {
            "dataType": ["text"],
            "description": "The filename of the document",
            "name": "filename",
        },
        {
            "dataType": ["text"],
            "description": "The title of the document",
            "name": "title",
        },
        {
            "dataType": ["text"],
            "description": "The document category",
            "name": "category",
        },
        {
            "dataType": ["text"],
            "description": "The text of the document",
            "name": "textVector",
        }
    ],
    "vectorizer": "text2vec-openai",
}

client.schema.create_class(class_obj)

schema = client.schema.get()
print(json.dumps(schema, indent=4))
