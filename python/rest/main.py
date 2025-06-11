from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Any
from games import dostepne_kluby
from games import play_game
from pydantic import BaseModel

class MyOwnModel(BaseModel):
    imie: str
    nazwisko:str

class GameData(BaseModel):
    klubAid: int
    klubBid: int
    wynikA: int
    wynikB: int
    stadion: str

# Replace this with your actual DB fetching function
def fetch_data_from_db() -> list[dict[str, Any]]:
    # Dummy example — replace with real DB call
    return [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"}
    ]





app = FastAPI() # Fluke, Django(*)

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

@app.get("/kluby")
def get_kluby():
    try:
        data = dostepne_kluby()
        return {"status": "success", "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.post("/play")
def play_one_game(data):
    try:
        #result = play_game(data.klubAid, data.klubBid, data.wynikA, data.wynikB, data.stadion)
        return {"status": "success", "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@app.post("/play2")
def play_one_game(data: MyOwnModel):
    try:
        #result = play_game(data.klubAid, data.klubBid, data.wynikA, data.wynikB, data.stadion)
        return {"status": "success", "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
