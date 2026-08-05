from fastapi import FastAPI

app = FastAPI(title="AI Interview Platform")

@app.get("/")
def home():
    return {"message": "Backend Running Successfully"}