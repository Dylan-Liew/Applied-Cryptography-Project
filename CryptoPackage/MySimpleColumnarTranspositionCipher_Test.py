# 190312k, Dylan Liew, DSF1901

from CryptoPackage import MySimpleColumnarTranspositionCipher

def run_test():
    print("===== Rail Fence Technique Testing =====")

    # Uppercase Character Testing
    plaintext = "HELLO"
    key = 100
    ciphertext = MySimpleColumnarTranspositionCipher.encrypt(plaintext,key)
    decryptedtext = MySimpleColumnarTranspositionCipher.decrypt(ciphertext,key)
    print("plaintext: " + plaintext)
    print("ciphertext: " + ciphertext)
    print("decryptedtext: " + decryptedtext + "\n")

    return


if __name__ == "__main__":
    run_test()





