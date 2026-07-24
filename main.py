from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def read_root(): #no input from the client is taken here
	return {"message": "Hello, world"} # fastapi will convert dict to json

