from fastapi import FastAPI
from pydantic import BaseModel
from uuid import uuid4 
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins= ["http://localhost:3000"],
    allow_methods= ["*"],
)


class TaskRead(BaseModel):
    id: str
    title: str
    completed: bool

class TaskCreate(BaseModel):
    title: str


tasks: list[TaskRead] = []

book = ''

@app.get("/tasks")
def read_tasks() -> list[TaskRead]:
    return tasks


@app.post("/tasks")
def create_tasks(payload: TaskCreate) -> TaskRead:
    new_task = TaskRead(id = str(uuid4()), title=payload.title, completed = False)

    tasks.append(new_task)
    return new_task


class BookCreate(BaseModel):
    book: str


@app.post("/book")
def create_book(payload: BookCreate):
    global book
    book = payload.book
    return book


@app.get("/book")
def read_book():
    return f"Любимая книга {book}"

