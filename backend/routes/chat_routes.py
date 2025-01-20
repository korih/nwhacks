from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from cloudflare import Cloudflare
import requests
import os

from utils.qdrant_helpers import search_text


chat = APIRouter()

CLOUDFLARE_API = os.getenv("CLOUDFLARE_API")
CLOUDFLARE_ID = os.getenv("CLOUDFLARE_ID")

API_BASE_URL = f"https://api.cloudflare.com/client/v4/accounts/{CLOUDFLARE_ID}/ai/run/"
headers = {"Authorization": f"Bearer {CLOUDFLARE_API}"}
client = Cloudflare(api_token=f"{CLOUDFLARE_API}")

class Msg(BaseModel):
	role: str
	content: str

def run(model, inputs):
	input = { "messages": inputs }
	response = requests.post(f"{API_BASE_URL}{model}", headers=headers, json=input)
	return response.json()

def build_responses(queries):
	q_a_responses = {}
	links = []
	
	for response in queries:
		answer = ""
		if response.instructor_answer != "Not Found":
#			print("instr")
			answer += f"Instructor Response: {response.instructor_answer}\n"

		if response.student_answer != "Not Found":
			answer += f"Student Response: {response.student_answer}\n"

		if answer == "":
			continue

		print(answer)
		links.append(response.link)
		q_a_responses[response.question] = answer
	
	q_a_responses["links"] = links
	return {"messages": q_a_responses, "links": links} 



inputs = [
#	test input
#	{ "role": "user", "content": "Write a short sentence about lazy brown fox, max 15 words"}
];

@chat.post('/api/chat/')
def api(msg: Msg):
	global inputs
	db_query = msg.content

	vector_db_query = search_text(db_query);
	response = build_responses(vector_db_query)
	q_a_response_prompts = str(response['messages'])
	links = str(response['links'])
	prompt = f"""
	Look at the following data:\n
	{q_a_response_prompts}

	Use the previous question and answers to answer this question only if it is relavent and you do not know the answer. If you do know the answer, just answer it with what you know: \n
	{msg.content}
	"""

	msg.content = prompt
	msg_string = msg.model_dump()
	inputs.append(msg_string)

	result = run("@cf/meta/llama-3.2-3b-instruct", inputs)
	result['links'] = links
	print(result)

	return JSONResponse({ "message": result }, status_code=200)

