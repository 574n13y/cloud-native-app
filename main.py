from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import uvicorn
from typing import List
import uuid
from datetime import datetime

app = FastAPI(title="Cloud Native App",
             description="A cloud-native FastAPI application",
             version="1.0.0")

templates = Jinja2Templates(directory="templates")

class HealthCheck(BaseModel):
    status: str
    version: str

class Task(BaseModel):
    id: str
    title: str
    description: str
    created_at: datetime

class TaskCreate(BaseModel):
    title: str
    description: str

# In-memory storage for tasks
tasks = []

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/health", response_model=HealthCheck)
async def health_check():
    return HealthCheck(
        status="healthy",
        version="1.0.0"
    )

@app.get("/tasks", response_model=List[Task])
async def get_tasks():
    return tasks

@app.post("/tasks", response_model=Task)
async def create_task(task: TaskCreate):
    new_task = Task(
        id=str(uuid.uuid4()),
        title=task.title,
        description=task.description,
        created_at=datetime.now()
    )
    tasks.append(new_task)
    return new_task

@app.delete("/tasks/{task_id}")
async def delete_task(task_id: str):
    for i, task in enumerate(tasks):
        if task.id == task_id:
            tasks.pop(i)
            return {"message": "Task deleted"}
    raise HTTPException(status_code=404, detail="Task not found")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
