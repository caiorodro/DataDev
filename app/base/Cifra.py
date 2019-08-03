from Crypto.Cipher import AES
from hashlib import md5
from Crypto import Random
from base64 import b64decode
from base64 import b64encode

key = '5896746505473791'
AV = 'Doran software31'

xkey = md5(key.encode('utf8')).hexdigest()

BLOCK_SIZE = 16

pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * \
            chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)

unpad = lambda s: s[:-ord(s[len(s) - 1:])]

def cifra(text):
    raw = pad(text)

    iv = Random.new().read(AES.block_size)
    cipher = AES.new(xkey, AES.MODE_CBC, iv)

    return b64encode(iv + cipher.encrypt(raw))

def decifra(text):
    enc = b64decode(text)
    iv = enc[:16]
    cipher = AES.new(xkey, AES.MODE_CBC, iv)

    plainText = unpad(cipher.decrypt(enc[16:])).decode('utf8')

    return plainText
