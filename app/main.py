from fastapi import FastAPI

app = FastAPI(
    title="FastAPI boilerplate"
)

@app.get("/")
def root():
    return {"message": "Welcome to the API!"}