import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

def main (): 
    #I decided to make this into an array of both the files to encrypt
    filesarray = ["mustang.bmp", "cp-logo.bmp"]

    for filename in filesarray:
        with open(filename, 'rb') as f:
            bmp_data = f.read()
        ##ecb way and output 
        #splitting the header file
        bmp_header = bmp_data[:54]
        image_data = bmp_data[54:]
        padded_image = pad(image_data, AES.block_size)
        key = get_random_bytes(16)
        iv = get_random_bytes(16)
    
        #ecbencryption and output 
        cipher_ecb = AES.new(key, AES.MODE_ECB)
        ciphertext_ecb = cipher_ecb.encrypt(padded_image)
        ecb_output = "ecb_" + filename
        with open(ecb_output, 'wb') as f:
            f.write(bmp_header + ciphertext_ecb)
    
        #cbc encryption and output
        cipher_cbc = AES.new(key, AES.MODE_CBC, iv)
        ciphertext_cbc = cipher_cbc.encrypt(padded_image)
        preblock = iv
        ##block by block encryption here , so using a for loopo to go through each one, i guess theres other ways to do it 
        for i in range(0, len(padded_image), AES.block_size):
            block = padded_image[i:i + AES.block_size]
            blocktoencrypt = bytes(a ^ b for a, b in zip(block, preblock))
            encrypted_block = cipher_cbc.encrypt(blocktoencrypt)
            ciphertext_cbc += encrypted_block
            preblock = encrypted_block

        cbc_output = "cbc_" + filename
        with open(cbc_output, 'wb') as f:
            f.write(bmp_header + ciphertext_cbc)

        #save the key and iv as binary file
        key_file = "key_" + filename[:-4] + ".bin"
        iv_file = "iv_" + filename[:-4] + ".bin"
        with open(key_file, 'wb') as f:
            f.write(key)
        with open(iv_file, 'wb') as f:
            f.write(iv)
        
        print("Processing:", filename)
        print("ECB output:", ecb_output)
        print("CBC output:", cbc_output)
        print("Key:", key.hex())
        print("IV:", iv.hex())
        
if __name__ == "__main__":     
    main()