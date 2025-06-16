from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Any
from games import dostepne_kluby
from games import play_game
from pydantic import BaseModel
from drop_database import delete 
from create_db import stworz_baze_danych_sport
from import_data import import_teams , import_players , import_all , import_coach , import_historia , import_games , import_rozgrywki
from transfer_player import dostepni_pilkarze , dostepni_pilkarze_z_danego_klubu
from transfer_coach import dostepni_trenerzy , trener_klubu
from gets import get_kluby,get_trenerzy, get_pilkarze , get_rozgrywki , get_mecze , get_historie , get_club_trener


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


###GET###  


@app.get("/data")
def get_data():
    try:
        data = fetch_data_from_db()
        return {"status": "success", "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/kluby")
def kluby():
    try:
        data = get_kluby()
        return {"status": "success", "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/pilkarze")
def pilkarze():
    try:
        data = get_pilkarze()
        return {"status": "success", "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/trenerzy")
def trenerzy():
    try:
        data = get_trenerzy()
        return {"status": "success", "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
 
@app.get("/rozgrywki")
def rozgrywki():
    try:
        data = get_rozgrywki()
        return {"status": "success", "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/historie")
def historia():
    try:
        data = get_historie()
        return {"status": "success", "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/mecze")
def mecze():
    try:
        data = get_mecze()
        return {"status": "success", "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

###GETY "zlozone"""

@app.get("/clubplayers")
def get_club_players(klub_id):
    try:
        data = dostepni_pilkarze_z_danego_klubu(klub_id)
        return {"status": "success", "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/clubtrener")
def get_trener_kluby(klub_id):
    try:
        data = get_club_trener(klub_id)
        return {"status": "success", "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



###POSTy###   
     
    
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
    
###NOWA BAZA DANYCH Z TABELAMI####
    
@app.post("/newdatabase")
def create_new_database():
    try:
        stworz_baze_danych_sport()
        return {"status": "success"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
###IMPORTY###

@app.post("/importplayers")
def import_new_players():
    try:
        import_players()
        return {"status": "success"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.post("/importcoach")
def import_new_coach():
    try:
        import_coach()
        return {"status": "success"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.post("/importgames")
def import_new_games():
    try:
        import_games()
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
    
@app.post("/importhisotry")
def import_new_history():
    try:
        import_historia()
        return {"status": "success"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.post("/importcimpetitions")
def import_new_competitions():
    try:
        import_rozgrywki()
        return {"status": "success"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


###IMPORT WSZYSTKO "na raz ####"

@app.post("/importalldata")
def import_all_data():
    try:
        import_all()
        return {"status": "success"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    


###DELETE##


    
@app.delete("/delete")
def delete_db():
    try:
        delete()
        return {"status": "success"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    


    

    


