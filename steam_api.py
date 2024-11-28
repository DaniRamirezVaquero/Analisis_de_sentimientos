import os
import requests
import json

archivo_juegos = 'steam_applist.json'

def get_app_list():
    
    url_api_steam = 'https://api.steampowered.com/ISteamApps/GetAppList/v2/'

    # Verificar si el archivo ya existe
    if not os.path.exists(archivo_juegos):
        print("Descargando listado de juegos desde la API de Steam...")
        response = requests.get(url_api_steam)
        data = response.json()
        
        if response.status_code == 200:
            with open(archivo_juegos, 'w') as f:
                json.dump(data, f)
            print("Listado de juegos descargado y guardado en 'steam_applist.json'.")
            
        else:
            print("Error al descargar el listado de juegos.")
          
        f.close()
        
    else:
        print("El archivo 'steam_applist.json' ya existe.")
        
    
        
def get_appid(game_name):
  # Cargar los datos del archivo JSON
    with open(archivo_juegos, 'r') as file:
        data = json.load(file)

    # Obtener la lista de juegos
    games = data['applist']['apps']

    # Buscar coincidencias exactas al inicio del nombre
    matches_start = [game for game in games if game['name'].lower().startswith(game_name.lower())]

    # Si no hay coincidencias exactas al inicio, buscar coincidencias en cualquier parte del nombre
    if len(matches_start) == 0:
        matches_contain = [game for game in games if game_name.lower() in game['name'].lower()]
    else:
        matches_contain = []

    matches = matches_start + matches_contain

    return matches