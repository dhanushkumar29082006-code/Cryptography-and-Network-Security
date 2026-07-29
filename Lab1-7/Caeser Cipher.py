text = input("Enter text: ")
key = int(input("Enter key: "))
encrypted = ""
for ch in text:
    if ch.isalpha():
        if ch.isupper():
            encrypted += chr((ord(ch) - 65 + key) % 26 + 65)
        else:
            encrypted += chr((ord(ch) - 97 + key) % 26 + 97)
    else:
        encrypted += ch

print("Encrypted Text:", encrypted)

decrypted = ""
for ch in encrypted:
    if ch.isalpha():
        if ch.isupper():
            decrypted += chr((ord(ch) - 65 - key) % 26 + 65)
        else:
            decrypted += chr((ord(ch) - 97 - key) % 26 + 97)
    else:
        decrypted += ch
print("Decrypted Text:", decrypted)