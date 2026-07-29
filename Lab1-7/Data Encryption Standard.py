from Crypto.Cipher import DES

key = b'12345678'

text = input("Enter Text: ")

while len(text) % 8 != 0:
    text += " "

des = DES.new(key, DES.MODE_ECB)

encrypted = des.encrypt(text.encode())
print("Encrypted:", encrypted.hex().upper())

decrypted = des.decrypt(encrypted)
print("Decrypted:", decrypted.decode().strip())
