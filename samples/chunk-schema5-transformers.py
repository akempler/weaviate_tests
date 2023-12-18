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
    "vectorizer": "text2vec-transformers",
    "moduleConfig": {
      "text2vec-transformers": {
        "vectorizeClassName": False
      }
    },
    "properties": [
        {
            "dataType": ["text"],
            "description": "A unique id of the index.",
            "name": "index_id",
            "moduleConfig": {
              "text2vec-transformers": {
                "skip": True,
                "vectorizePropertyName": False
              }
            }
        },
        {
            "dataType": ["int"],
            "description": "The sequential index of the chunk in the text.",
            "name": "chunk_sequence",
            "moduleConfig": {
              "text2vec-transformers": {
                "skip": True,
                "vectorizePropertyName": False
              }
            }
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
            "moduleConfig": {
              "text2vec-transformers": {
                "skip": True,
                "vectorizePropertyName": False
              }
            }
        },
        {
            "dataType": ["text"],
            "description": "The type of entity.",
            "name": "entity_type",
            "moduleConfig": {
              "text2vec-transformers": {
                "skip": True,
                "vectorizePropertyName": False
              }
            }
        },
        {
            "dataType": ["text"],
            "description": "The entity bundle.",
            "name": "bundle",
            "moduleConfig": {
              "text2vec-transformers": {
                "skip": True,
                "vectorizePropertyName": False
              }
            }
        },
        {
            "dataType": ["text"],
            "description": "An optional parent entity of the entity the chunk belongs to.",
            "name": "parent_entity_id",
            "moduleConfig": {
              "text2vec-transformers": {
                "skip": True,
                "vectorizePropertyName": False
              }
            }
        },
        {
            "dataType": ["text"],
            "description": "The type of entity of the parent entity.",
            "name": "parent_entity_type",
            "moduleConfig": {
              "text2vec-transformers": {
                "skip": True,
                "vectorizePropertyName": False
              }
            }
        },
    ],
}

client.schema.create_class(class_obj)

schema = client.schema.get()
print(json.dumps(schema, indent=4))
