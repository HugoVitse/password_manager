from Crypto.Cipher import AES
import hashlib
import json

def inputToKey(inp : str) -> bytes:
    
    hash_input = hashlib.sha512()
    
    hash_input.update(inp.encode())

    key = hash_input.hexdigest()[0:16].encode()
    
    return key


def encrypt(plain : dict ,inp : str) -> tuple[bytes,bytes,bytes]:
    
    encode = json.dumps(plain).encode()

    key = inputToKey(inp)

    cipher = AES.new(key, AES.MODE_EAX)

    nonce = cipher.nonce

    ciphertext, tag = cipher.encrypt_and_digest(encode)
    
    return ciphertext, tag, nonce

    
def decrypt(cipher : bytes,inp : str,tag : bytes,nonce : bytes) -> dict:
    
    key = inputToKey(inp)

    decryptor = AES.new(key, AES.MODE_EAX, nonce=nonce)

    plaintext = decryptor.decrypt(cipher)

    try:

        decryptor.verify(tag)

        return json.loads(plaintext.decode())

    except ValueError:

        return "error"
