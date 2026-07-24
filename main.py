from fastapi import FastAPI, HTTPException

tasks = [
    {"id": 1, "title": "Complete WAF assignments", "done": False},
    {"id": 2, "title": "GIT repo create for proj: Portfolio app", "done": True},
    {"id": 3, "title": "Clean the table", "done": False}
]

app = FastAPI()

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
