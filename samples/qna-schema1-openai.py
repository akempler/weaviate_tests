import weaviate
import json

with open('./keys/openai_key.txt', 'r') as f:
    api_tkn = f.read().strip()

client = weaviate.Client(
    url="http://localhost:8080/",
)

# ===== add schema ===== 
class_obj = {
    "class": "Qna",
    "description": "QnA for querying.",
    "vectorizer": "text2vec-openai",
    "moduleConfig": {
      "text2vec-openai": {
        "vectorizeClassName": False
      },
      "qna-openai": {
          "model": "gpt-3.5-turbo-instruct",
          "maxTokens": 50
        }
    },
    "properties": [
        {
            "dataType": ["text"],
            "description": "The unique id of the index.",
            "name": "index_id",
            "moduleConfig": {
              "text2vec-openai": {
                "skip": True,
                "vectorizePropertyName": False
              }
            }
        },
        {
            "dataType": ["text"],
            "description": "The title/question of the qna",
            "name": "title",
        },
        {
            "dataType": ["text"],
            "description": "The text/answer of the qna",
            "name": "body",
        },
        {
            "dataType": ["text"],
            "description": "The id of the entity the qna belongs to.",
            "name": "entity_id",
            "moduleConfig": {
              "text2vec-openai": {
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
              "text2vec-openai": {
                "skip": True,
                "vectorizePropertyName": False
              }
            }
        },
        {
            "dataType": ["text"],
            "description": "The parent entity of the entity the qna belongs to.",
            "name": "parent_entity_id",
            "moduleConfig": {
              "text2vec-openai": {
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
              "text2vec-openai": {
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
