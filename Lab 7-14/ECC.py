from cryptography.hazmat.primitives.asymmetric import ec
private1 = ec.generate_private_key(ec.SECP256R1())
private2 = ec.generate_private_key(ec.SECP256R1())
secret1 = private1.exchange(ec.ECDH(), private2.public_key())
secret2 = private2.exchange(ec.ECDH(), private1.public_key())
print("Shared Secret Match:", secret1 == secret2)