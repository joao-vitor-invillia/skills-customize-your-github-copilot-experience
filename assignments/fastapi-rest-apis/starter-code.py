"""Starter code: Building REST APIs with FastAPI.

Run locally:
    uvicorn starter-code:app --reload
"""

from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel, Field

app = FastAPI(title="Tasks API")


class TaskCreate(BaseModel):
    title: str = Field(..., min_length=3)
    done: bool = False


class Task(TaskCreate):
    id: int


tasks: list[Task] = []
next_id = 1


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Welcome to the Tasks API"}


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(payload: TaskCreate) -> Task:
    global next_id
    task = Task(id=next_id, **payload.model_dump())
    tasks.append(task)
    next_id += 1
    return task


@app.get("/tasks", response_model=list[Task])
def list_tasks() -> list[Task]:
    return tasks


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int) -> Task:
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")


@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, payload: TaskCreate) -> Task:
    for index, task in enumerate(tasks):
        if task.id == task_id:
            updated = Task(id=task_id, **payload.model_dump())
            tasks[index] = updated
            return updated
    raise HTTPException(status_code=404, detail="Task not found")


@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int) -> Response:
    for index, task in enumerate(tasks):
        if task.id == task_id:
            del tasks[index]
            return Response(status_code=status.HTTP_204_NO_CONTENT)
    raise HTTPException(status_code=404, detail="Task not found")
