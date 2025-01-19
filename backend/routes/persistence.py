from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from cloudflare import Cloudflare
from sqlalchemy.orm import Session
from models.modal import User, SessionLocal
from models.chats import Chat
from typing import List, Dict
import requests

chat = APIRouter()

class UserCreate(BaseModel):
	name: str
	email: str

class MsgCreate(BaseModel):
	title: str
	user: str
	messages: List[Dict[str,str]] 

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def query_chats(username: str, chatname: str, db: Session = Depends(get_db)):
	chat = db.query(Chat).filter(Chat.username == username, Chat.title == chatname).first()
	return chat
@chat.post("/api/users/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
	new_user = User(name=user.name, email=user.email)
	try:
		db.add(new_user)
		db.commit()
		db.refresh(new_user)
		return new_user
	except:
		return JSONResponse({ "message": "User already Exists"}, status_code=400)


@chat.get("/api/users/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_db)):
	return db.query(User).filter(User.id == user_id).first()

@chat.post("/api/log/")
def create_chat(chat: MsgCreate, db: Session = Depends(get_db)):
	existing_chats = query_chats(chat.user, chat.title)
	if existing_chats:
		existing_chats.messages.extend(chat.messages)
		db.commit()
		db.refresh(existing_chats)
		return existing_chats
	else:
		new_chat = Chat(title=chat.title, messages=chat.messages)
		db.add(new_chat)
		db.commit()
		db.refresh(new_chat)
		return new_chat
