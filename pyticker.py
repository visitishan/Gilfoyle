import requests
from playsound import playsound
from time import sleep
from os import system, name
from config import * 

infinite = 1
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
	if (ok >= upper_limit or ok < lower_limit):
		playsound('alert.mp3')
	else:
		print('<')
	clear()
	print('Price of '+ coin + ' in INR is -   Rs. ' + str(ok))
	sleep(refresh_interval)
