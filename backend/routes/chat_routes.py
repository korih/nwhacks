from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from cloudflare import Cloudflare
import requests
import os


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

inputs = [
#	test input
#	{ "role": "user", "content": "Write a short sentence about lazy brown fox, max 15 words"}
];

@chat.post('/api/chat/')
def api(msg: Msg):
	inputs.append(msg.model_dump())

	result = run("@cf/meta/llama-3.2-3b-instruct", inputs)

	return JSONResponse({ "message": result}, status_code=200)

