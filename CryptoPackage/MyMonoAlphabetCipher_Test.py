# 190312k, Dylan Liew, DSF1901

from CryptoPackage import MyMonoAlphabetCipher

def run_test():
    print("===== Mono-Alphabet Cipher Testing =====")

    plaintext = "Supercalifragilisticexpialidocious"
    # Optional Input on Key
    # shuffled_alphabets = "BWEMDSYOUVZRXNAIHTQLPGCFJK"
    ciphertext = MyMonoAlphabetCipher.encrypt(plaintext)
    decryptedtext = MyMonoAlphabetCipher.decrypt(ciphertext)
    print("plaintext: " + plaintext)
    print("ciphertext: " + ciphertext)
    print("decryptedtext: " + decryptedtext + "\n")
    print("")
    return


if __name__ == "__main__":
    run_test()
