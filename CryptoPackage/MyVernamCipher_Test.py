# 190312k, Dylan Liew, DSF1901

from CryptoPackage import MyVernamCipher


def run_test():
    print("===== Vernam Cipher Testing =====")
    plaintext = "HELLO"
    key = "APPLE"
    ciphertext = MyVernamCipher.encrypt(plaintext,key)
    decryptedtext = MyVernamCipher.decrypt(ciphertext,key)
    print("plaintext: " + plaintext)
    print("ciphertext: " + ciphertext)
    print("decryptedtext: " + decryptedtext + "\n")

    return


if __name__ == "__main__":
    run_test()
