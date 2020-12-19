# 190312k, Dylan Liew, DSF1901

from CryptoPackage import MyCaesarCipher


def run_test():
    print("===== Caesar Cipher Testing =====")
    key = 13

    # Uppercase Character Testing
    plaintext = "HELLO"
    ciphertext = MyCaesarCipher.encrypt(key, plaintext)
    decryptedtext = MyCaesarCipher.decrypt(key, ciphertext)
    print("plaintext: " + plaintext)
    print("ciphertext: " + ciphertext)
    print("decryptedtext: " + decryptedtext + "\n")

    # Lowercase Character Testing
    plaintext = "Hello"
    ciphertext = MyCaesarCipher.encrypt(key, plaintext)
    decryptedtext = MyCaesarCipher.decrypt(key, ciphertext)
    print("plaintext: " + plaintext)
    print("ciphertext: " + ciphertext)
    print("decryptedtext: " + decryptedtext + "\n")

    return


if __name__ == "__main__":
    run_test()
