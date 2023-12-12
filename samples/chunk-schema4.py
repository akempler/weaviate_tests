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
    "vectorizer": "text2vec-openai",
    "moduleConfig": {
      "text2vec-openai": {
        "model": "gpt-4-1106-preview"
      },
      "qna-openai": {
        "model": "gpt-4-1106-preview", 
        "temperature": 0.6
      }
    },
    "properties": [
        {
            "dataType": ["int"],
            "description": "The sequential index of the chunk in the text.",
            "name": "chunk_sequence",
        },
        {
            "dataType": ["text"],
            "description": "The chunk of text",
            "name": "chunk",
        },
        {
            "dataType": ["text"],
            "description": "The id of the entity the chunk belongs to.",
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
        },
        {
            "dataType": ["text"],
            "description": "An optional parent entity of the entity the chunk belongs to.",
            "name": "parent_entity_id",
        },
        {
            "dataType": ["text"],
            "description": "The type of entity.",
            "name": "parent_entity_type",
        },
    ],
    "vectorizer": "text2vec-openai",
}

client.schema.create_class(class_obj)

schema = client.schema.get()
print(json.dumps(schema, indent=4))
