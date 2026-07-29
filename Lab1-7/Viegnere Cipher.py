text = input("Enter Text: ").upper()
key = input("Enter Key: ").upper()
# Encryption
cipher = ""
for i in range(len(text)):
    cipher += chr(((ord(text[i])-65) + (ord(key[i % len(key)])-65)) % 26 + 65)
print("Encrypted:", cipher)
# Decryption
plain = ""
for i in range(len(cipher)):
    plain += chr(((ord(cipher[i])-65) - (ord(key[i % len(key)])-65)) % 26 + 65)
print("Decrypted:", plain)
