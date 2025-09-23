from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {
        "message": "base project initialized",
        "version": "1.0.0"
    }