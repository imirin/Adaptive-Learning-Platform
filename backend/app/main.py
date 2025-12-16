from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List


app = FastAPI()

# Allow React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/health")
def health_check():
    return {"status": "Backend is healthy"}

@app.get("/api/learning-path")
def learning_path():
    return {
        "user": "Irin",
        "level": "Beginner",
        "recommended_topics": [
            "Python Basics",
            "Data Structures",
            "Algorithms",
            "AI Fundamentals"
        ]
    }

from pydantic import BaseModel

class SkillInput(BaseModel):
    python: int
    dsa: int
    ai: int

@app.post("/api/assess-skill")
def assess_skill(data: SkillInput, username: str):
    avg_score = (data.python + data.dsa + data.ai) / 3

    if avg_score < 40:
        level = "Beginner"
        path = ["Python Basics", "Loops & Functions", "Basic DSA"]
    elif avg_score < 70:
        level = "Intermediate"
        path = ["Advanced Python", "Trees & Graphs", "ML Basics"]
    else:
        level = "Advanced"
        path = ["System Design", "Deep Learning", "AI Projects"]

    result = {
        "python": data.python,
        "dsa": data.dsa,
        "ai": data.ai,
        "level": level
    }

    if username in users_db:
        users_db[username]["assessments"].append(result)

    return {
        "level": level,
        "recommended_path": path
    }

# Temporary in-memory database
users_db = {}

@app.post("/api/create-user")
def create_user(username: str):
    if username in users_db:
        return {"message": "User already exists"}

    users_db[username] = {
        "assessments": []
    }

    return {"message": f"User {username} created successfully"}

@app.get("/api/user-progress")
def user_progress(username: str):
    if username not in users_db:
        return {"error": "User not found"}

    return {
        "username": username,
        "assessments": users_db[username]["assessments"]
    }
