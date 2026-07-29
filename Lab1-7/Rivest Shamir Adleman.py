p = 17
q = 11

n = p * q
e = 3
d = 107

msg = input("Enter Message: ")

cipher = []
for ch in msg:
    cipher.append(pow(ord(ch), e, n))

print("Encrypted:", cipher)

plain = ""
for c in cipher:
    plain += chr(pow(c, d, n))

print("Decrypted:", plain) 