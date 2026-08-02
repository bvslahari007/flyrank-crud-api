from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3


tasks = [
    {"id": 1, "title": "Complete WAF assignments", "done": False},
    {"id": 2, "title": "GIT repo create for proj: Portfolio app", "done": True},
    {"id": 3, "title": "Clean the table", "done": False}
]

app = FastAPI()

conn = sqlite3.connect("tasks.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
	CREATE TABLE IF NOT EXISTS tasks(
		id INTEGER PRIMARY KEY,
		title TEXT,
		done INTEGER
	)
""")

cursor.execute("SELECT COUNT(*) FROM tasks")
count = cursor.fetchone()[0]


@app.get("/")
def read_root(): 
	return {"name": "Task API", "version": "1.0", "endpoints":["/tasks"]} 

@app.get("/health")
def health():
	return {"status": "ok"}

@app.get("/tasks")
def get_tasks():
	return tasks

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
	for task in tasks:
		if task['id'] == task_id:
			return task
	raise HTTPException(status_code=404, detail=f"Task {task_id} not found")


class TaskCreate(BaseModel):  #defines a shape called TaskCreatea
	title: str #anything claiming to be this shape must have a field called title

@app.post("/tasks", status_code=201)
def create_task(new_task: TaskCreate):
	if (new_task.title == ""):
		raise HTTPException(status_code=400, detail="No task found to add")
	else:
		new_id = tasks[-1]['id'] + 1
		new_task_dict = {"id":new_id, "title": new_task.title,"done":False}
		tasks.append(new_task_dict)
		return new_task_dict

class TaskUpdate(BaseModel):
	title: str | None = None
	done: bool | None = None 

@app.put("/tasks/{task_id}")
def update_task(task_id: int, up_task:TaskUpdate):
	for task in tasks:
		if task['id'] == task_id:
			if up_task.title is not None:
				task['title'] = up_task.title
			if up_task.done is not None:
				task['done'] = up_task.done
			return task
	raise HTTPException(status_code=404, detail=f"Task {task_id} not found")


@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
	for task in tasks:
		if task['id'] == task_id:
			tasks.remove(task)
			return
	raise HTTPException(status_code=404, detail=f"Task {task_id} not found")

# tested with swagger ui
