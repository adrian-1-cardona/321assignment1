from operator import xor
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
 
key = get_random_bytes(16)
iv = get_random_bytes(16)
 
def submit(strinput):
    strinput = strinput.replace(';', '%3b').replace('=', '%3d')
    plaintext = "userid=456;userdata=" + strinput + ";session-id=31337"
    padded = pad(plaintext.encode(), AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return cipher.encrypt(padded)
 
def verify(uinput):
    euserin = bytearray(euserin)
    euserin[4] = xor(euserin[4], 0x63)
    euserin[10] = xor(euserin[10], 0x65)
    
    euserin = bytes(euserin)
    
    mode = AES.new(key, AES.MODE_CBC, iv)
    decryptedString = mode.decrypt(euserin)
    
    #ignore errors 
    decryptedString = unpad(decryptedString, 16).decode(errors='ignore')
    
    return ";admin=true;" in decryptedString

if __name__ == "__main__":
    string = submit("XadminXtrue")
    string = verify(string)
    print(string)