# 190312k, Dylan Liew, DSF1901
alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabets += alphabets.lower()


def encrypt(plaintext, shuffled_alphabets="BWEMDSYOUVZRXNAIHTQLPGCFJK"):
    # Allow both uppercase and lowercase character
    shuffled_alphabets.upper()
    shuffled_alphabets += shuffled_alphabets.lower()

    ciphertext = ""
    for character in plaintext:
        # Find the index of each character and replace it with the new character with same index
        position = alphabets.find(character)
        if position == -1:
            ciphertext += " "
        else:
            ciphertext += shuffled_alphabets[position]
    return ciphertext


def decrypt(ciphertext, shuffled_alphabets="BWEMDSYOUVZRXNAIHTQLPGCFJK"):
    # Allow both uppercase and lowercase character
    shuffled_alphabets.upper()
    shuffled_alphabets += shuffled_alphabets.lower()
    plaintext = ""
    for character in ciphertext:
        # Find the index of each character and replace it with the new character with same index
        position = shuffled_alphabets.find(character)
        if position == -1:
            plaintext += " "
        else:
            plaintext += alphabets[position]
    return plaintext
