import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

def main (): 
    #I decided to make this into an array of both the files to encrypt
    filesarray = ["mustang.bmp", "cp-logo.bmp"]
    for filename in filesarray:
        encryptbmpfile(filename)

def encryptbmpfile(filename):
    with open(filename, 'rb') as f:
        bmp_data = f.read()
    
    #preserve bmp header 
    bmp_header = bmp_data[:54]
    image_data = bmp_data[54:]
    
    #generate randon key,iv and pad the image 
    key = get_random_bytes(16)
    iv = get_random_bytes(16)
    padded_image = pad(image_data, AES.block_size)
    
    #ecb encryption
    cipher_ecb = AES.new(key, AES.MODE_ECB)
    ciphertext_ecb = cipher_ecb.encrypt(padded_image)
    ecb_output = f"ecb_{filename}"
    with open(ecb_output, 'wb') as f:
        f.write(bmp_header + ciphertext_ecb)
    
    # CBC Encryption (Manual implementation using ECB + XOR)
    cipher_ecb_cbc = AES.new(key, AES.MODE_ECB)
    ciphertext_cbc = b''
    previous_block = iv  # IV is the "previous ciphertext" for first block
    
    # Process each 16-byte block
    for i in range(0, len(padded_image), AES.block_size):
        block = padded_image[i:i + AES.block_size]
        # XOR plaintext block with previous ciphertext block
        xored_block = bytes(a ^ b for a, b in zip(block, previous_block))
        # Encrypt the XORed block using ECB
        encrypted_block = cipher_ecb_cbc.encrypt(xored_block)
        ciphertext_cbc += encrypted_block
        previous_block = encrypted_block  # This ciphertext becomes the previous block
    
    cbc_output = f"cbc_{filename}"
    with open(cbc_output, 'wb') as f:
        f.write(bmp_header + ciphertext_cbc)
        
if __name__ == "__main__":     
    main()