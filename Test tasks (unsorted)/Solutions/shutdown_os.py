# restart os
import os

restart = input('Shutdown (yes/no)?')

if restart == 'no':
    exit()
else:
    os.system('shutdown /s /t 5')
