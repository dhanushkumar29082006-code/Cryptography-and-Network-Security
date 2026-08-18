from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import pad, unpad
key = b"mysecretkey"
text = input("Enter Text: ")
cipher = Blowfish.new(key, Blowfish.MODE_ECB)
encrypted = cipher.encrypt(pad(text.encode(), 8))
print("Encrypted:", encrypted.hex())
decrypted = unpad(cipher.decrypt(encrypted), 8)
print("Decrypted:", decrypted.decode())