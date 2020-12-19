# 190312k, Dylan Liew, DSF1901
import math
def encrypt(plaintext, key):
    # Create Matrix of Plaintext using Key as Column
    matrix = [["" for i in range(key)] for j in range(int(math.ceil(len(plaintext)/key)))]
    index = 0
    for col in matrix:
        for j in range(key):
            if index < len(plaintext):
                col[j] = plaintext[index]
                index += 1

    # Obtain Ciphertext Using Matrix
    index = 0
    ciphertext = ""
    for x in range(key):
        for i in matrix:
            ciphertext += i[index]
        index += 1
    return ciphertext

def decrypt(ciphertext, key):
    row = int(math.ceil(len(ciphertext)/key))
    value = int(len(ciphertext)//key)
    if value == 0:
        value += 1
    matrix = [["" for i in range(key)] for j in range(value)]
    x = len(ciphertext) % key
    if x > 0:
        matrix.append(["" for i in range(x)])
    list_index = 0
    text_index = 0
    chr_index = 0
    for i in range(row):
        for j in range(key):
            if text_index < len(ciphertext):
                if x > 0:
                    if chr_index >= x and list_index == row-1:
                        pass
                    else:
                        matrix[list_index][chr_index] = ciphertext[text_index]
                        text_index += 1
                else:
                    matrix[list_index][chr_index] = ciphertext[text_index]
                    text_index += 1

                if list_index < row-1:
                    list_index += 1
                else:
                    list_index = 0
                    chr_index += 1
    plaintext = ""
    for i in matrix:
        plaintext += "".join(i)
    return plaintext


