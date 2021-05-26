# restart os
import os

restart = input('Restart (yes/no)?')

if restart == 'no':
    exit()
else:
    os.system('shutdown /r /t 5')
