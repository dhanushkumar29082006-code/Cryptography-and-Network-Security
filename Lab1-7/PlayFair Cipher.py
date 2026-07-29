key = "MONARCHY"
text = "HELLO"

matrix = [
    ['M','O','N','A','R'],
    ['C','H','Y','B','D'],
    ['E','F','G','I','K'],
    ['L','P','Q','S','T'],
    ['U','V','W','X','Z']
]

def find(ch):
    if ch == 'J':
        ch = 'I'
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == ch:
                return i, j

cipher = ""

for i in range(0, len(text), 2):
    a = text[i].upper()
    b = text[i + 1].upper() if i + 1 < len(text) else 'X'

    r1, c1 = find(a)
    r2, c2 = find(b)

    if r1 == r2:
        cipher += matrix[r1][(c1 + 1) % 5]
        cipher += matrix[r2][(c2 + 1) % 5]
    elif c1 == c2:
        cipher += matrix[(r1 + 1) % 5][c1]
        cipher += matrix[(r2 + 1) % 5][c2]
    else:
        cipher += matrix[r1][c2]
        cipher += matrix[r2][c1]

print("Cipher Text:", cipher)