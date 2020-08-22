import os
from tqdm import tqdm
from time import sleep
import pyfiglet
os.system('color 0A')
#Text in default font
out = pyfiglet.figlet_format("Hacking Started !!!")
print(out)


for char in tqdm(range(1,150)):
    sleep(0.25)

out = pyfiglet.figlet_format("Hacked !!!")
print(out)


