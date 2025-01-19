import os, json
from models.piazza_post import PiazzaPost
from qdrant_client import QdrantClient

COLLECTION_NAME = "piazza_embeddings"

qdrant_client = QdrantClient(
	url="https://1016ac99-4665-4067-b806-1fce7ed81e19.us-east4-0.gcp.cloud.qdrant.io:6333", 
	api_key=os.environ.get("QDRANT_KEY"),
)

def upload_documents():
	folder_path="assets/piazza_posts"

	if not os.path.exists(folder_path):
		print(f"Cannot upload documents, path: {folder_path} does not exist!")
		return

	piazza_posts:list[PiazzaPost] = []
	for filename in os.listdir(folder_path):
		file_path = os.path.join(folder_path, filename)
		try:
			with open(file_path, 'r') as json_file:
				data = json.load(json_file)
				piazza_posts.append(PiazzaPost(**data))
		except Exception as e:
			print(f"Failed to process {file_path}, {e}")

	piazza_posts_metadata:list[dict] = []
	piazza_posts_body:list[str] = []
	for post in piazza_posts:
		piazza_posts_body.append(post.body)
		piazza_posts_metadata.append({
		    "author": post.author,
		    "position": post.position,
		    "course": post.course,
		    "post_num": post.post_num,
		    "link": post.link
		})
		
	qdrant_client.add(
		collection_name=COLLECTION_NAME,
		documents=piazza_posts_body,
		metadata=piazza_posts_metadata
	)

def delete_collection():
	qdrant_client.delete_collection(COLLECTION_NAME)

def search_text(text: str) -> list[PiazzaPost]:
	search_result = qdrant_client.query(
	    collection_name=COLLECTION_NAME,
	    query_text=text,
	    limit=10
	)

	piazza_posts:list[PiazzaPost] = []
	for result in search_result:
		piazza_posts.append(PiazzaPost(
		    author=result.metadata["author"],
		    position=result.metadata["position"],
		    course=result.metadata["course"],
		    post_num=result.metadata["post_num"],
		    link=result.metadata["link"],
		    body=result.document
		))
	return piazza_posts

def misc():
	pass
	# delete_collection()
	# docs = ["I love africa! I love the hot sun!", "The north pole is very cold, you can build an Igloo."]
	# metadata = [
	# 	{"source": "CPSC 418 2024 W1"},
	# 	{"source": "CPSC 418 2024 W1"}
	# ]
	# qdrant_client.add(
	# 	collection_name=COLLECTION_NAME,
	# 	documents=docs,
	# 	metadata=metadata
	# )
	# search_result = qdrant_client.query(
	#     collection_name=COLLECTION_NAME,
	#     query_text="snow",
	#     limit=2
	# )
	# print(search_result)
