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

schema = client.schema.get()
#print(json.dumps(schema, indent=4))


#some_objects = client.data_object.get()
#print(json.dumps(some_objects, indent=4))

# client.data_object.get()

nearText = {"concepts": ["pregnant"]}

result = (
    client.query
    .get("Question", ["question", "answer", "category"])
    .with_near_text(nearText)
    .with_limit(2)
    .do()
)

print(json.dumps(result, indent=4))

# result = (client.query.get("Question", ["question answer"]).do())
# print(json.dumps(result, indent=4))

ask = {
  "question": "Can I be fired?",
  "properties": ["question"]
}

result = (
  client.query
  .get("Question", ["answer"])
  .with_ask(ask)
  .with_limit(2)
  .do()
)

print(json.dumps(result, indent=4))
