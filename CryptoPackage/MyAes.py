# 190312k, Dylan Liew, DSF1901
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64
def get_fixed_key():
    # use fixed AES key, 256 bits
    return b"01234567890123456789012345678901"

# AES Keysize [16*8,24*8,32*8]
def get_random_key(keysize):
    """ generate random AES key, keysize = 32*8 = 256 bits"""
    return get_random_bytes(keysize)


# AES encrypt using Selected Mode and IV with default padding (PKCS7)
def encrypt(key, plaintext_utf8, mode):
    #  Electronic Code Book (ECB)
    plaintext_utf8 = plaintext_utf8.encode("utf8")
    if mode == "ECB":
        cipher = AES.new(key, AES.MODE_ECB)
        ciphertext = cipher.encrypt(pad(plaintext_utf8, AES.block_size))
        return base64.b64encode(ciphertext).decode('utf-8')
    # Cipher Block Chaining (CBC)
    elif mode == "CBC":
        cipher = AES.new(key, AES.MODE_CBC)
        ciphertext = cipher.encrypt(pad(plaintext_utf8, AES.block_size))
        result = cipher.iv + ciphertext
        return base64.b64encode(result).decode('utf-8')

    # Cipher Feedback (CFB)
    elif mode == "CFB":
        cipher = AES.new(key, AES.MODE_CFB)
        ciphertext = cipher.encrypt(pad(plaintext_utf8, AES.block_size))
        result = cipher.iv + ciphertext
        return base64.b64encode(result).decode('utf-8')

    # Output Feedback (OFB)
    elif mode == "OFB":
        cipher = AES.new(key, AES.MODE_OFB)
        ciphertext = cipher.encrypt(pad(plaintext_utf8, AES.block_size))
        result = cipher.iv + ciphertext
        return base64.b64encode(result).decode('utf-8')




# AES decrypt using CBC and IV, with default unpadding (PKCS7)
def decrypt(key, ciphertext_string, mode):
    # Electronic Code Book (ECB)
    if mode == "ECB":
        ciphertext = base64.b64decode(ciphertext_string)
        cipher = AES.new(key, AES.MODE_ECB)
        decryptedtext_utf = unpad(cipher.decrypt(ciphertext), AES.block_size)
        return decryptedtext_utf.decode("utf8")
    # Cipher Block Chaining (CBC)
    elif mode == "CBC":
        iv = base64.b64decode(ciphertext_string)[:16]
        ciphertext = base64.b64decode(ciphertext_string)[16:]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decryptedtext_utf = unpad(cipher.decrypt(ciphertext), AES.block_size)
        return decryptedtext_utf.decode("utf8")
    # Cipher Feedback (CFB)
    elif mode == "CFB":
        iv = base64.b64decode(ciphertext_string)[:16]
        ciphertext = base64.b64decode(ciphertext_string)[16:]
        cipher = AES.new(key, AES.MODE_CFB, iv)
        decryptedtext_utf = unpad(cipher.decrypt(ciphertext), AES.block_size)
        return decryptedtext_utf.decode("utf8")
    # Output Feedback (OFB)
    elif mode == "OFB":
        iv = base64.b64decode(ciphertext_string)[:16]
        ciphertext = base64.b64decode(ciphertext_string)[16:]
        cipher = AES.new(key, AES.MODE_OFB, iv)
        decryptedtext_utf = unpad(cipher.decrypt(ciphertext), AES.block_size)
        return decryptedtext_utf.decode("utf8")
