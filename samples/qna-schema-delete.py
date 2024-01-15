import weaviate
import json

client = weaviate.Client(
    url="http://localhost:8080/",
)

# print(client)
print("Deleting schema...")

# v4
# Delete existing schema (if necessary - THIS WILL ALSO DELETE ALL OF YOUR DATA)
# if (client.collections.exists("Chunk")):
#   client.collections.delete("Chunk")  # Replace with your collection name

# v3
client.schema.delete_class("Qna")

# Fetch & inspect schema (should be empty)
schema = client.schema.get()
print(json.dumps(schema, indent=4))
