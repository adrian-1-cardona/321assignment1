import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

# List of BMP files to encrypt
target_files = ["mustang.bmp", "cp-logo.bmp"]

for filename in target_files:
    with open(filename, 'rb') as f:
            bmp_data = f.read()
    
    # Split header (first 54 bytes) from image data
    bmp_header = bmp_data[:54]
    image_data = bmp_data[54:]
    
    # Pad the image data
    padded_image = pad(image_data, AES.block_size)
    
    # Generate random key and IV
    key = get_random_bytes(16)
    iv = get_random_bytes(16)
    
    # ECB encryption
    cipher_ecb = AES.new(key, AES.MODE_ECB)
    ciphertext_ecb = cipher_ecb.encrypt(padded_image)
    
    # Write ECB output file
    ecb_output = "ecb_" + filename
    with open(ecb_output, 'wb') as f:
        f.write(bmp_header + ciphertext_ecb)
    
    # CBC encryption
    cipher_cbc = AES.new(key, AES.MODE_CBC, iv)
    ciphertext_cbc = cipher_cbc.encrypt(padded_image)
    
    # Write CBC output file
    cbc_output = "cbc_" + filename
    with open(cbc_output, 'wb') as f:
        f.write(bmp_header + ciphertext_cbc)
    
    # Save key and IV for reference
    key_file = "key_" + filename[:-4] + ".bin"
    iv_file = "iv_" + filename[:-4] + ".bin"
    with open(key_file, 'wb') as f:
        f.write(key)
    with open(iv_file, 'wb') as f:
        f.write(iv)
    
    # Simple print statements
    print("Processing:", filename)
    print("ECB output:", ecb_output)
    print("CBC output:", cbc_output)
    print("Key:", key.hex())
    print("IV:", iv.hex())