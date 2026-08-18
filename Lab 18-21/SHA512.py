import hashlib
text = input("Enter Text: ")
result = hashlib.sha512(text.encode())
print("SHA512 Hash Value:")
print(result.hexdigest())