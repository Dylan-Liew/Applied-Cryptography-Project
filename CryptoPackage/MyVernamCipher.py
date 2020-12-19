# 190312k, Dylan Liew, DSF1901
characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encrypt(plaintext, key):
    plaintext = plaintext.upper()
    key = key.upper()
    ciphertext = ""
    for i in range(len(key)):
        total_index = characters.find(plaintext[i]) + characters.find(key[i])
        if total_index > 25:
            total_index -= 26
        ciphertext += characters[total_index]
    return ciphertext


def decrypt(ciphertext, key):
    ciphertext = ciphertext.upper()
    key = key.upper()
    plaintext = ""
    for i in range(len(key)):
        total_index = characters.find(ciphertext[i]) - characters.find(key[i])
        if total_index < 0:
            total_index += 26
        plaintext += characters[total_index]
    return plaintext

