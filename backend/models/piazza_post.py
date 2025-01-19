from pydantic import BaseModel

class PiazzaPost(BaseModel):
	author: str
	position: str
	course: str
	post_num: int
	link: str
	body: str

class PiazzaPostResult(BaseModel):
	author: str
	position: str
	course: str
	post_num: int
	link: str
	body: str
	score: float
