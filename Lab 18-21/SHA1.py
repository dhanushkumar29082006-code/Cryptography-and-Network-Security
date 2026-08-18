import hashlib
text = input("Enter Text: ")
result = hashlib.sha1(text.encode())
print("SHA1 Hash Value:")
print(result.hexdigest())