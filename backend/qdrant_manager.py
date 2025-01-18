import os
# Set working directory to this file
os.chdir(os.path.dirname(os.path.abspath(__file__)))

from dotenv import load_dotenv
load_dotenv()
import argparse
from utils.qdrant_helpers import upload_documents, delete_collection, search_text, misc

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
		"-s", "--search",
		nargs="+",
		help="Perform vector search with some text"
	)
	parser.add_argument(
		"-m", "--misc",
		action="store_true",
		help="Scratch function I can change for developing"
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
