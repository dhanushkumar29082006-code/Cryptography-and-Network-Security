key = [
    [6, 24, 1],
    [13, 16, 10],
    [20, 17, 15]
]

text = input("Enter 3 letters: ").upper()

p = [ord(text[0]) - 65,
     ord(text[1]) - 65,
     ord(text[2]) - 65]

cipher = ""

for i in range(3):
    value = 0
    for j in range(3):
        value += key[i][j] * p[j]

    cipher += chr((value % 26) + 65)

print("Cipher Text:", cipher)
