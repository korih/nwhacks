import os
# Set working directory to this file
os.chdir(os.path.dirname(os.path.abspath(__file__)))

from dotenv import load_dotenv
load_dotenv()
import argparse
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

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Manages QDrant DB.")
	parser.add_argument(
		"-u", "--upload",
		action="store_true",
		help="Uploads all the documents in assets/piazza_posts/*.txt to QDrant"
	)
	parser.add_argument(
		"-d", "--delete",
		action="store_true",
		help="Deletes the collection and all the documents"
	)
	parser.add_argument(
		"-m", "--misc",
		action="store_true",
		help="Scratch function I can change for developing"
	)
	parser.add_argument(
		"-s", "--search",
		nargs="+",
		help="Perform vector search with some text"
	)

	args = parser.parse_args()

	if args.upload:
		upload_documents()
	if args.delete:
		delete_collection()
	if args.search:
		query_text = " ".join(args.search)
		search_text(query_text)
	if args.misc:
		misc()

	if not any(vars(args).values()):
		parser.print_help()
