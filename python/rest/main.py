from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Any

# Replace this with your actual DB fetching function
def fetch_data_from_db() -> list[dict[str, Any]]:
    # Dummy example — replace with real DB call
    return [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"}
    ]

app = FastAPI()

# Optional: Allow frontend to access backend (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or specify your frontend domain
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/data")
def get_data():
    try:
        data = fetch_data_from_db()
        return {"status": "success", "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/test")
def get_test(name):
    try:
        data = {"name" : name}
        return {"status": "success", "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.post("/apppost")
def appPost(data):
    try:
        data = {"data" : data}
        return {"status": "success", "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

