import weaviate
import json

client = weaviate.Client(
    url="http://localhost:8080/",
)

# Delete existing schema (if necessary - THIS WILL ALSO DELETE ALL OF YOUR DATA)
client.schema.delete_all()

# Fetch & inspect schema (should be empty)
schema = client.schema.get()
print(json.dumps(schema, indent=4))
