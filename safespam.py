# SafeSpam
# 16 Oct, 2020
# Developed by Rohit Chouhan
# https://github.com/rohit-chouhan

import sys 
from termcolor import colored, cprint
import requests
import colorama
colorama.init()
cprint('   _____        __      _____                       ','yellow')
cprint('  / ____|      / _|    / ____|                      ','yellow')
cprint(' | (___   __ _| |_ ___| (___  _ __   __ _ _ __ ___  ','yellow')
cprint('  \___ \ / _  |  _/ _ \\___ \|  _ \ / _  |  _ ` _ \ ','yellow')
cprint('  ____) | (_| | ||  __/____) | |_) | (_| | | | | | |','yellow')
cprint(' |_____/ \__,_|_| \___|_____/| .__/ \__,_|_| |_| |_|','yellow')
cprint('                             | |                    ','yellow')
cprint('                             |_|                    ','yellow')

cprint('Developed by Rohit Chouhan','green')
cprint('____________________________________\n','white')
cprint('Enter Email::','red','on_yellow')
email = input()
response = requests.get("https://www.validator.pizza/email/"+email)
if response.json()["status"]==400 :
    cprint('\n'+email+' IS INVALID EMAIL','yellow','on_red')
else :
   if response.json()["disposable"]==True:
      cprint('\n'+email+' IS NOT SAFE','white','on_red')
   else :
      cprint('\n'+email+' IS SAFE','white','on_green')

input('Press ENTER to exit')