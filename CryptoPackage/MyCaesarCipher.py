# 190312k, Dylan Liew, DSF1901
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'    # Q1, Q2, Q3

def encrypt(key, plaintext_utf8):
    ciphertext_utf8 = ""

    for character in plaintext_utf8:
        if character.isupper():
            if character in LETTERS:
                # get the character position
                position = LETTERS.find(character)
                position = position + key

                # wrap-around if position >= length of LETTERS
                while position >= len(LETTERS):
                    position = position - len(LETTERS)

                # append encrypted character
                ciphertext_utf8 = ciphertext_utf8 + LETTERS[position]

            else:
                # append character without encrypting
                ciphertext_utf8 = ciphertext_utf8 + character
        else:
            if character.upper() in LETTERS:
                # get the character position
                position = LETTERS.find(character.upper())
                position = position + key

                # wrap-around if position >= length of LETTERS
                while position >= len(LETTERS):
                    position = position - len(LETTERS)

                # append encrypted character
                ciphertext_utf8 += LETTERS[position].lower()

            else:
                # append character without encrypting
                ciphertext_utf8 += character

    return ciphertext_utf8


def decrypt(key, ciphertext_utf8):
    decryptedtext_utf = ""

    for character in ciphertext_utf8:
        if character.isupper():
            if character in LETTERS:
                # get the character position
                position = LETTERS.find(character)
                position = position - key
                # wrap-around if position >= length of LETTERS
                while position < 0 :
                    position = position + len(LETTERS)

                # append encrypted character
                decryptedtext_utf = decryptedtext_utf + LETTERS[position]

            else:
                # append character without encrypting
                decryptedtext_utf = decryptedtext_utf + character
        else:
            if character.upper() in LETTERS:
                # get the character position
                position = LETTERS.find(character.upper())
                position = position - key
                # wrap-around if position >= length of LETTERS
                while position < 0 :
                    position = position + len(LETTERS)

                # append encrypted character
                decryptedtext_utf += LETTERS[position].lower()

            else:
                # append character without encrypting
                decryptedtext_utf += character
    return decryptedtext_utf


