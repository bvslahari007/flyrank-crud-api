from fastapi import FastAPI, HTTPException
from model import TaskCreate, TaskUpdate

app = FastAPI()

@app.get("/")
def read_root():
    return {"name": "Task API", "version": "1.0", "endpoints": ["/tasks"]}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/tasks")
def get_tasks():
    pass

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    pass

@app.post("/tasks", status_code=201)
def create_task(new_task: TaskCreate):
    pass

@app.put("/tasks/{task_id}")
def update_task(task_id: int, up_task: TaskUpdate):
    pass

@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    pass

# tested with swagger ui   