# Commande prérequis : pip install fastapi uvicorn requests
# uvicorn main:app --reload

from fastapi import FastAPI, Query
import requests

app = FastAPI()

# Clé API
API_KEY = "live_qZdccCPJXIFVr3a4kke4EvQ8Mi00wjmI6qydKtHtWtY18mUWiiIQzicXh2N9qh39" 

# URL des chats
CAT_API_URL = "https://api.thecatapi.com/v1/images/search"

@app.get("/")
def home():
    return {"message": "Bienvenue sur notre API python de photos de chats !"}


# Récupère un nombre de photos :
# Exemple : http://127.0.0.1:8000/external-data?limit=3 --> 3 photos
@app.get("/external-data")
def get_external_data(limit: int = Query(5, description="Nombre d'images à récupérer")):
    headers = {"x-api-key": API_KEY} if API_KEY else {}
    params = {"limit": limit} 
    response = requests.get(CAT_API_URL, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        print("Données brutes reçues : ", data)  # Affichage
        return data[:limit] 
    return {"error": "Impossible de récupérer les données."}



# Récupère 5 images max > 500px de largeur :
# Exemple : http://127.0.0.1:8000/filtered-data?limit=5 --> 5 photos > 500px de large
@app.get("/filtered-data")
def get_filtered_data(limit: int = Query(5, description="Nombre d'images à récupérer")):
    headers = {"x-api-key": API_KEY} if API_KEY else {}
    response = requests.get(CAT_API_URL, params={"limit": limit}, headers=headers)
    if response.status_code == 200:
        data = response.json()
        filtered_data = [
            item for item in data if item.get("width", 0) > 500
        ]
        return filtered_data
    return {"error": "Impossible de récupérer les données."}

