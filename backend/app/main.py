from fastapi import FastAPI

app = FastAPI(
    title="Operations Management System API",
    version="1.0.0",
    description="Backend API for the Operations Management System"
)


@app.get("/")
def root():
    return {
        "message": "Welcome to Operations Management System API"
    }