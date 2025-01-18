import os
from qdrant_client import QdrantClient

COLLECTION_NAME = "piazza_embeddings"

qdrant_client = QdrantClient(
	url="https://1016ac99-4665-4067-b806-1fce7ed81e19.us-east4-0.gcp.cloud.qdrant.io:6333", 
	api_key=os.environ.get("QDRANT_KEY"),
)


def upload_documents():
	pass

def delete_collection():
	qdrant_client.delete_collection(COLLECTION_NAME)

def search_text(text: str):
	search_result = qdrant_client.query(
	    collection_name=COLLECTION_NAME,
	    query_text=text,
	    limit=10
	)

	for result in search_result:
		print(f"score: {result.score}")
		print(f"document: {result.document} \n")
	

def misc():
	delete_collection()
	docs = ["I love africa! I love the hot sun!", "The north pole is very cold, you can build an Igloo."]
	metadata = [
		{"source": "CPSC 418 2024 W1"},
		{"source": "CPSC 418 2024 W1"}
	]
	qdrant_client.add(
		collection_name=COLLECTION_NAME,
		documents=docs,
		metadata=metadata
	)
	search_result = qdrant_client.query(
	    collection_name=COLLECTION_NAME,
	    query_text="snow",
	    limit=2
	)
	print(search_result)
