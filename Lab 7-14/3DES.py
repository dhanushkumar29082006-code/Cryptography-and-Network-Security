text = input("Enter Text: ")
k1 = "key12345"
k2 = "pass6789"
k3 = "abc12345"
encrypted = ""
for i in range(len(text)):
    c = ord(text[i]) ^ ord(k1[i % 8])
    c ^= ord(k2[i % 8])
    c ^= ord(k3[i % 8])
    encrypted += chr(c)
print("Encrypted:", encrypted)
decrypted = ""
for i in range(len(encrypted)):
    c = ord(encrypted[i]) ^ ord(k3[i % 8])
    c ^= ord(k2[i % 8])
    c ^= ord(k1[i % 8])
    decrypted += chr(c)
print("Decrypted:", decrypted)