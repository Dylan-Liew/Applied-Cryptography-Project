# 190312k, Dylan Liew, DSF1901

from CryptoPackage import MyRailFenceTechnique

def run_test():
    print("===== Rail Fence Technique Testing =====")

    # Uppercase Character Testing
    plaintext = "HELLO WORLD"
    key = 7
    ciphertext = MyRailFenceTechnique.encrypt(plaintext,key)
    decryptedtext = MyRailFenceTechnique.decrypt(ciphertext,key)
    print("plaintext: " + plaintext)
    print("ciphertext: " + ciphertext)
    print("decryptedtext: " + decryptedtext + "\n")

    return


if __name__ == "__main__":
    run_test()



