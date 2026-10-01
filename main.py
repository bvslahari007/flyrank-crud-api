from fastapi import FastAPI, HTTPException
from model import TaskCreate, TaskUpdate
from repository import PostgresRepository

app = FastAPI()
repo = PostgresRepository()

@app.get("/")
def read_root():
    return {"name": "Task API", "version": "1.0", "endpoints": ["/tasks"]}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/tasks")
def get_tasks():
    res = repo.get_all_tasks()
    if len(res) == 0:
        raise HTTPException(status_code=404, detail="No tasks found")
    return res

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    res = repo.get_task_by_id(task_id)
    if res is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return res

@app.post("/tasks", status_code=201)
def create_task(new_task: TaskCreate):
    res = repo.create_task(new_task)
    if res is None:
        raise HTTPException(status_code=400, detail="Task creation failed")
    return res

@app.put("/tasks/{task_id}")
def update_task(task_id: int, up_task: TaskUpdate):
    res = repo.update_task(task_id, up_task)
    if res is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return res

@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    res = repo.delete_task(task_id)
    if res is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return {
    "deleted_id": task_id}

# tested with swagger ui   