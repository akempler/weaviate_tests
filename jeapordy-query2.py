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

ask = {
  "question": "What animals weigh the most?",
  "properties": ["question"]
}

result = (
  client.query
  .get("Question", ["answer", "_additional {answer {hasAnswer certainty property result startPosition endPosition} }"])
  .with_ask(ask)
  .with_limit(2)
  .do()
)

print(json.dumps(result, indent=4))

# Use a graphql query inline:
# # https://weaviate.io/developers/weaviate/api/graphql/explore
# explore_articles_query = """
#   {
#     Explore (
#       nearText: {
#         concepts: ["heaviest animals"],
#       }
#     ) {
#       beacon
#       certainty 
#       distance 
#       className
#     }
#   }
# """

# query_result = client.query.raw(explore_articles_query)
# print(query_result)