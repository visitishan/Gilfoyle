import requests
from playsound import playsound
from time import sleep
from os import system, name 

infinite = 1
coin = 'BTC'
r = requests.get('https://koinex.in/api/ticker')
jsonfile = r.json()
ok = jsonfile['prices']['inr'][coin]
ok = int(ok)

#clear screen function 
def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 


while(infinite==1):
	if ok >= 26000:
		playsound('alert.mp3')
	else:
		print('<')
	clear()
	print(ok)
	sleep(5)
