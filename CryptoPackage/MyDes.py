# 190312k, Dylan Liew, DSF1901
from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64

# DES Keysize [16*8,24*8,32*8]
def get_random_key():
    """ generate random DES key, keysize = 32*8 = 256 bits"""
    return get_random_bytes(8)


# DES encrypt using Selected Mode and IV with default padding (PKCS7)
def encrypt(key, plaintext_utf8, mode):
    plaintext_utf8 = plaintext_utf8.encode("utf8")
    #  Electronic Code Book (ECB)
    if mode == "ECB":
        cipher = DES.new(key, DES.MODE_ECB)
        ciphertext = cipher.encrypt(pad(plaintext_utf8, DES.block_size))
        return base64.b64encode(ciphertext).decode('utf-8')
    # Cipher Block Chaining (CBC)
    elif mode == "CBC":
        cipher = DES.new(key, DES.MODE_CBC)
        ciphertext = cipher.encrypt(pad(plaintext_utf8, DES.block_size))
        result = cipher.iv + ciphertext
        return base64.b64encode(result).decode('utf-8')

    # Cipher Feedback (CFB)
    elif mode == "CFB":
        cipher = DES.new(key, DES.MODE_CFB)
        ciphertext = cipher.encrypt(pad(plaintext_utf8, DES.block_size))
        result = cipher.iv + ciphertext
        return base64.b64encode(result).decode('utf-8')

    # Output Feedback (OFB)
    elif mode == "OFB":
        cipher = DES.new(key, DES.MODE_OFB)
        ciphertext = cipher.encrypt(pad(plaintext_utf8, DES.block_size))
        result = cipher.iv + ciphertext
        return base64.b64encode(result).decode('utf-8')




# DES decrypt using CBC and IV, with default unpadding (PKCS7)
def decrypt(key, ciphertext_string, mode):
    # Electronic Code Book (ECB)
    if mode == "ECB":
        ciphertext = base64.b64decode(ciphertext_string)
        cipher = DES.new(key, DES.MODE_ECB)
        decryptedtext_utf = unpad(cipher.decrypt(ciphertext), DES.block_size)
        return decryptedtext_utf.decode("utf8")
    # Cipher Block Chaining (CBC)
    elif mode == "CBC":
        iv = base64.b64decode(ciphertext_string)[:8]
        ciphertext = base64.b64decode(ciphertext_string)[8:]
        cipher = DES.new(key, DES.MODE_CBC, iv)
        decryptedtext_utf = unpad(cipher.decrypt(ciphertext), DES.block_size)
        return decryptedtext_utf.decode("utf8")
    # Cipher Feedback (CFB)
    elif mode == "CFB":
        iv = base64.b64decode(ciphertext_string)[:8]
        ciphertext = base64.b64decode(ciphertext_string)[8:]
        cipher = DES.new(key, DES.MODE_CFB, iv)
        decryptedtext_utf = unpad(cipher.decrypt(ciphertext), DES.block_size)
        return decryptedtext_utf.decode("utf8")
    # Output Feedback (OFB)
    elif mode == "OFB":
        iv = base64.b64decode(ciphertext_string)[:8]
        ciphertext = base64.b64decode(ciphertext_string)[8:]
        cipher = DES.new(key, DES.MODE_OFB, iv)
        decryptedtext_utf = unpad(cipher.decrypt(ciphertext), DES.block_size)
        return decryptedtext_utf.decode("utf8")
