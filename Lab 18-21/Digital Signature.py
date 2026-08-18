import hashlib
message = input("Enter Message: ")
n = 143
e = 7
d = 103
hash_value = int(hashlib.sha1(message.encode()).hexdigest(), 16)
signature = pow(hash_value, d, n)
print("Digital Signature:", signature)
verified_hash = pow(signature, e, n)
if verified_hash == (hash_value % n):
    print("Signature Verified")
else:
    print("Verification Failed")