import os
import pikepdf
import pyfiglet
from tqdm import tqdm
from tqdm import tqdm
from time import sleep

os.system("color 0A")
# Text in default font
out = pyfiglet.figlet_format("Hacking Started !!!")
print(out)

passwords = [line.strip() for line in open("common-password.txt")]

isPasswordFound = False
FoundPassword = ""
# iterate over passwords
for password in tqdm(passwords, "Decrypting"):
    try:
        # open PDF file
        with pikepdf.open("test-doc.pdf", password=password) as pdf:
            # Password decrypted successfully, break out of the loop
            isPasswordFound = True
            FoundPassword = password
            break
    except pikepdf._qpdf.PasswordError as e:
        # wrong password, just continue in the loop
        continue


if isPasswordFound == True:
    text = f"Password found : {FoundPassword}"
    out = pyfiglet.figlet_format(text)
    print(out)
else:
    text = f"Not found"
    out = pyfiglet.figlet_format(text)
    print(out)
