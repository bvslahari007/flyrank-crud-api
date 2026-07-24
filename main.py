from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def read_root(): #no input from the client is taken here
	return {"name": "Task API", "version": "1.0", "endpoints":["/tasks"]} # fastapi will convert dict to json

@app.get("/health")
def health():
	return {"status": "ok"}
