import os
import json
import requests


hostname = os.uname().nodename

firebase_url = 'https://hostname-5c24b-default-rtdb.firebaseio.com/hostname/export.json'

response = requests.get(firebase_url, headers={'Cache-Control': 'no-cache'})
data = response.json()

if data is not None and 'host' in data and data['host'] == hostname:
    print("Host ya Guardado")
else:
    # Crear el objeto JSON
    json_data = {
        "host": hostname
    }

    response = requests.patch(firebase_url, json=json_data)
    if response.status_code == 200:
        print("El host se conecto exitosamente")
    else:
        print("Error al conectar con el host")

