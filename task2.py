from operator import xor
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
 
key = get_random_bytes(16)
iv = get_random_bytes(16)
 
def submit(strinput):
    strinput = strinput.replace(';', '%3b').replace('=', '%3d')
    plaintext = "userid=456; userdata=" + strinput + " ;session-id=31337"
    padded = pad(plaintext.encode(), AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return cipher.encrypt(padded)
 
def verify(ciphertext):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded = cipher.decrypt(ciphertext)
    plaintext = unpad(padded, AES.block_size).decode()
    return ";admin=true;" in plaintext