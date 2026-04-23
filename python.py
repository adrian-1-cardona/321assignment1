import os
from base64 import b64encode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# Generate random key and IV
key = get_random_bytes(16)  # 128-bit key
iv = get_random_bytes(16)   # 128-bit IV for CBC

# Read the BMP file
with open('cp-logo.bmp', 'rb') as f:
    bmp_data = f.read()

# Split header (first 54 bytes) from image data
bmp_header = bmp_data[:54]
image_data = bmp_data[54:]

# Pad the image data
padded_image = pad(image_data, AES.block_size)
#then encrypt it 
cipher_ecb = AES.new(key, AES.MODE_ECB)
ciphertext_ecb = cipher_ecb.encrypt(padded_image)

# Write ECB output file (header + encrypted image)
with open('cp-logo_ecb.bmp', 'wb') as f:
    f.write(bmp_header + ciphertext_ecb)
