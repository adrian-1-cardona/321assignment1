from Cryptodome.Cipher import AES

def encrypt(key, plaintext):
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(plaintext.encode('utf-8'))
    return (cipher.nonce, tag, ciphertext)
def decrypt(key, nonce, tag, ciphertext):
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)
    return plaintext.decode('utf-8')
# Example usage
key = b'sixteen byte key'  # Must be 16, 24, or 32 bytes long
plaintext = "Hello, World!"
nonce, tag, ciphertext = encrypt(key, plaintext)
print("Ciphertext:", ciphertext)
decrypted_text = decrypt(key, nonce, tag, ciphertext)
print("Decrypted text:", decrypted_text)
