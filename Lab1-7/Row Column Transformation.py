text = input("Enter Plain Text: ")
# Encryption
cipher = text[::2] + text[1::2]
print("Encrypted Text :", cipher)
# Decryption
n = len(text)
mid = (n + 1) // 2
first = cipher[:mid]
second = cipher[mid:]
plain = ""
for i in range(mid):
    plain += first[i]
    if i < len(second):
        plain += second[i]
print("Decrypted Text :", plain) 
