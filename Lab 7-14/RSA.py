p = 11
q = 13

n = p * q
e = 7
d = 103

msg = input("Enter Message: ")

cipher = [pow(ord(ch), e, n) for ch in msg]
print("Encrypted:", cipher)

plain = "".join(chr(pow(c, d, n)) for c in cipher)
print("Decrypted:", plain)