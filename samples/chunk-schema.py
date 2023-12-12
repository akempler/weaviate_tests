import weaviate
import json

with open('./keys/openai_key.txt', 'r') as f:
    api_tkn = f.read().strip()

client = weaviate.Client(
    url="http://localhost:8080/",
)

# ===== add schema ===== 
class_obj = {
    "class": "Chunk",
    "description": "Chunks of text from website pages.",
    "properties": [
        {
            "dataType": ["text"],
            "description": "The chunk of text",
            "name": "chunk",
        },
        {
            "dataType": ["text"],
            "description": "The id of the topic the chunk belongs to.",
            "name": "topic_id",
        },
        {
            "dataType": ["text"],
            "description": "The id of the entity",
            "name": "entity_id",
        },
        {
            "dataType": ["text"],
            "description": "The type of entity.",
            "name": "entity_type",
        },
        {
            "dataType": ["text"],
            "description": "The entity bundle.",
            "name": "bundle",
        }
    ],
    "vectorizer": "text2vec-openai",
}

client.schema.create_class(class_obj)

schema = client.schema.get()
print(json.dumps(schema, indent=4))
