# 190312k, Dylan Liew, DSF1901

from CryptoPackage import MyDes
import random
modes = ["ECB", "CBC", "CFB", "OFB"]


def run_test():
    print("===== DES Testing =====")
    key = MyDes.get_random_key()
    # key = "12345678".encode('utf-8')
    mode = "ECB"
    plaintext_string = "Testing DES encrypt and decrypt."
    # encode plaintext, then encrypt
    ciphertext_string = MyDes.encrypt(key, plaintext_string, mode)
    # decrypt ciphertext, then decode
    decryptedtext_string = MyDes.decrypt(key, ciphertext_string, mode)
    print("mode: "+mode)
    print("plaintext: " + plaintext_string)
    print("ciphertext: " + ciphertext_string)
    print("decryptedtext: " + decryptedtext_string)
    print("")

    key = MyDes.get_random_key()
    mode = "CBC"
    plaintext_string = "Testing DES encrypt and decrypt."
    ciphertext_string = MyDes.encrypt(key, plaintext_string, mode)
    decryptedtext_string = MyDes.decrypt(key, ciphertext_string, mode)
    print("mode: "+mode)
    print("plaintext: " + plaintext_string)
    print("ciphertext: " + ciphertext_string)
    print("decryptedtext: " + decryptedtext_string)
    print("")

    key = MyDes.get_random_key()
    mode = "CFB"
    plaintext_string = "Testing DES encrypt and decrypt."
    ciphertext_string = MyDes.encrypt(key, plaintext_string, mode)
    decryptedtext_string = MyDes.decrypt(key, ciphertext_string, mode)
    print("mode: "+mode)
    print("plaintext: " + plaintext_string)
    print("ciphertext: " + ciphertext_string)
    print("decryptedtext: " + decryptedtext_string)
    print("")

    key = MyDes.get_random_key()
    mode = "OFB"
    plaintext_string = "Testing DES encrypt and decrypt."
    ciphertext_string = MyDes.encrypt(key, plaintext_string, mode)
    decryptedtext_string = MyDes.decrypt(key, ciphertext_string, mode)
    print("mode: "+mode)
    print("plaintext: " + plaintext_string)
    print("ciphertext: " + ciphertext_string)
    print("decryptedtext: " + decryptedtext_string)
    print("")
    return


if __name__ == "__main__":
    run_test()
