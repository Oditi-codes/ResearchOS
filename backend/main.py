from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

class PaperCreate(BaseModel):
    title: str
    authors: list[str]
    abstract: str

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Welcome to ResearchOS!"}

@app.post("/papers")
def create_paper(paper: PaperCreate):
    return {
        "id": 1,
        "title": paper.title,
        "authors": paper.authors,
        "abstract": paper.abstract,
        "status": "created"
    }

