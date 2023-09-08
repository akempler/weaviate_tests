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


ask = {
  "question": "Who was the detective in the case?",
  "properties": ["category", "filename", "textVector"]
}

result = (
  client.query
  .get("JudicialDocument", ["filename", "_additional {answer {hasAnswer certainty property result startPosition endPosition} }"])
  .with_ask(ask)
  .with_limit(1)
  .do()
)

print(json.dumps(result, indent=4))
