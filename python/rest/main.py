from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Any
from games import dostepne_kluby
from games import play_game
from pydantic import BaseModel
from drop_database import delete 
from create_db import stworz_baze_danych_sport
from import_data import import_teams , import_coach
from transfer_player import dostepni_pilkarze
from transfer_coach import dostepni_trenerzy


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
    
@app.post("/delete")
def delete_db():
    try:
        delete()
        return {"status": "success"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.post("/newdatabase")
def create_new_database():
    try:
        stworz_baze_danych_sport()
        return {"status": "success"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.post("/importteams")
def import_new_teams():
    try:
        import_teams()
        return {"status": "success"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/pilkarze")
def get_pilkarze():
    try:
        data = dostepni_pilkarze()
        return {"status": "success", "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/trenerzy")
def get_trenerzy():
    try:
        data = dostepni_trenerzy()
        return {"status": "success", "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    


