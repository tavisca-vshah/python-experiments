import pikepdf
from tqdm import tqdm

passwords = [line.strip() for line in open("wordlistwithlength3.txt")]

# iterate over passwords
for password in tqdm(passwords, "Decrypting PDF"):
    try:
        # open PDF file
        with pikepdf.open("sample1234.pdf", password=password) as pdf:
            # Password decrypted successfully, break out of the loop
            print("Password found:", password)
            break
    except pikepdf._qpdf.PasswordError as e:
        # wrong password, just continue in the loop
        continue
