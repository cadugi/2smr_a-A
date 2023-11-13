import rsa

# Generate public and private keys
(public_key, private_key) = rsa.newkeys(512)

# Convert public key to password
password = public_key.save_pkcs1().decode()

# Print public and private keys
print("Public key (password):", password)
print("Private key:", private_key.save_pkcs1().decode())