from fastapi import FastAPI

# Create an instance of the FastAPI application
app = FastAPI(
    title="FastAPI Beginner's Toolkit",
    description="A minimal working example for the Moringa AI Capstone Project.",
    version="1.0.0",
)


# Root endpoint — returns a welcome message
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI World!"}


# Dynamic endpoint — accepts item_id as a path parameter
# and an optional 'q' query parameter
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}
