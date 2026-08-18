p = 23
g = 5
a = 6
b = 15
A = (g ** a) % p
B = (g ** b) % p
key1 = (B ** a) % p
key2 = (A ** b) % p
print("Alice Key:", key1)
print("Bob Key:", key2)