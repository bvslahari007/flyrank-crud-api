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
if count == 0:
	cursor.execute("INSERT INTO tasks (title, done) VALUES (?, ?)", ("Clean the table", 0))
	cursor.execute("INSERT INTO tasks (title, done) VALUES (?, ?)", ("Complete WAF assignment", 0))
	cursor.execute("INSERT INTO tasks (title, done) VALUES (?, ?)", ("CN Wireshark implementation", 0))
	conn.commit()

@app.get("/")
def read_root(): 
	return {"name": "Task API", "version": "1.0", "endpoints":["/tasks"]} 

@app.get("/health")
def health():
	return {"status": "ok"}

@app.get("/tasks")
def get_tasks():
	cursor.execute("SELECT * FROM tasks")
	rows = cursor.fetchall()
	result = []
	for row in rows:
		task = {"id": row[0], "title": row[1], "done": row[2]}
		result.append(task)
	return result

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
	cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
	row = cursor.fetchone()
	if row is None:
		raise HTTPException(status_code=404, detail=f"Task {task_id} not found")
	return {"id": row[0], "title": row[1], "done": row[2]}

class TaskCreate(BaseModel):  #defines a shape called TaskCreatea
	title: str #anything claiming to be this shape must have a field called title

@app.post("/tasks", status_code=201)
def create_task(new_task: TaskCreate):
	if new_task.title == "":
		raise HTTPException(status_code=400, detail="Task not mentioned properly")
	cursor.execute("INSERT INTO tasks (title, done) VALUES (?, ?)", (new_task.title, 0))
	conn.commit()
	new_id = cursor.lastrowid
	return {"id": new_id, "title": new_task.title, "done": 0}

class TaskUpdate(BaseModel):
	title: str | None = None
	done: bool | None = None 

@app.put("/tasks/{task_id}")
def update_task(task_id: int, up_task:TaskUpdate):
	cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
	row = cursor.fetchone()
	if row is None:
		raise HTTPException(status_code=404, detail=f"Task {task_id} not found")
	new_title = up_task.title if up_task.title is not None else row[1]
	new_done = up_task.done if up_task.done is not None else row[2]

	cursor.execute("UPDATE tasks SET title = ?, done = ? WHERE id = ?", (new_title, new_done, task_id))
	conn.commit()
	return {"id": task_id, "title": new_title, "done": new_done}

@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
	cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
	row = cursor.fetchone()
	if row is None:
		raise HTTPException(status_code=404, detail=f"Task {task_id} not found")
	cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
	conn.commit()
	return	

# tested with swagger ui
