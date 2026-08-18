import hashlib
text = input("Enter Text: ")
result = hashlib.md5(text.encode())
print("MD5 Hash Value:")
print(result.hexdigest())