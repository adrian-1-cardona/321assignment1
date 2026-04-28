from operator import xor
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
 
key = get_random_bytes(16)
iv = get_random_bytes(16)

#submit function that takes in the user input and does the entire replace thing from the instrcutions
def submit(strinput):
    strinput = strinput.replace(';', '%3b').replace('=', '%3d')
    plaintext = "userid=456;userdata=" + strinput + ";session-id=31337"
    padded = pad(plaintext.encode(), AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return cipher.encrypt(padded)
 
 #verify function that takes in the encrypted user input and does the entire decryption and unpad thing from the instructions
def verify(uinput):
    uinput = bytearray(uinput)
    uinput[4] = xor(uinput[4], 0x63)
    uinput[10] = xor(uinput[10], 0x65)
    
    uinput = bytes(uinput)
    
    mode = AES.new(key, AES.MODE_CBC, iv)
    decryptedString = mode.decrypt(uinput)
    
    decryptedString = unpad(decryptedString, 16).decode(errors='ignore')
    
    return ";admin=true;" in decryptedString

if __name__ == "__main__":
    string = submit("XadminXtrue")
    string = verify(string)
    print(string)