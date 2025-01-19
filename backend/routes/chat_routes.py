from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from cloudflare import Cloudflare
from sse_starlette.sse import EventSourceResponse
import requests
import time

chat = APIRouter()

API_BASE_URL = "https://api.cloudflare.com/client/v4/accounts/ff2fcbe7e481ecb5d9bbb7668ceb7904/ai/run/"

class Msg(BaseModel):
	role: str
	content: str

def run(model, inputs):
    input = { "messages": inputs }
    response = requests.post(f"{API_BASE_URL}{model}", headers=headers, json=input)
    return response.json()


inputs = [
#	test input
#	{ "role": "user", "content": "Write a short sentence about lazy brown fox, max 15 words"}
];

@chat.post('/api/chat')
def api(msg: Msg):
	inputs.append(msg.model_dump())

	result = run("@cf/meta/llama-3.2-3b-instruct", inputs)

	return JSONResponse({ "message": result}, status_code=200)
