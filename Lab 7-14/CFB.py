from Crypto.Cipher import DES
key = b"12345678"
iv = b"abcdefgh"
text = input("Enter Text: ")
cipher = DES.new(key, DES.MODE_CFB, iv)
encrypted = cipher.encrypt(text.encode())
print("Encrypted:", encrypted.hex())
cipher = DES.new(key, DES.MODE_CFB, iv)
decrypted = cipher.decrypt(encrypted)
print("Decrypted:", decrypted.decode())