from pydantic import BaseModel

class PiazzaPost(BaseModel):
	author: str
	position: str
	course: str
	post_num: int
	link: str
	title: str
	question: str
	student_answer: str
	instructor_answer: str

class PiazzaPostResult(BaseModel):
	author: str
	position: str
	course: str
	post_num: int
	link: str
	title: str
	question: str
	student_answer: str
	instructor_answer: str
	score: float
