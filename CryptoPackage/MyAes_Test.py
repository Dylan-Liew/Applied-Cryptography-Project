# 190312k, Dylan Liew, DSF1901

from CryptoPackage import MyAes
import random
key_sizes = [16, 24, 32]
modes = ["ECB", "CBC", "CFB", "OFB"]


def run_test():
    print("===== AES Testing =====")
    # key = MyAes.get_random_key(random.choice(key_sizes))
    key = "1234567890123456".encode('utf-8')
    mode = "ECB"
    plaintext_string = "Testing AES encrypt and decrypt."
    # encode plaintext, then encrypt
    ciphertext_string = MyAes.encrypt(key, plaintext_string, mode)
    # decrypt ciphertext, then decode
    decryptedtext_string = MyAes.decrypt(key, ciphertext_string, mode)
    print("mode: " + mode)
    print("plaintext: " + plaintext_string)
    print("ciphertext: " + ciphertext_string)
    print("decryptedtext: " + decryptedtext_string)
    print("")

    key = MyAes.get_random_key(random.choice(key_sizes))
    mode = "CBC"
    plaintext_string = "Testing AES encrypt and decrypt."
    ciphertext_string = MyAes.encrypt(key, plaintext_string, mode)
    decryptedtext_string = MyAes.decrypt(key, ciphertext_string, mode)
    print("mode: " + mode)
    print("plaintext: " + plaintext_string)
    print("ciphertext: " + ciphertext_string)
    print("decryptedtext: " + decryptedtext_string)
    print("")

    key = MyAes.get_random_key(random.choice(key_sizes))
    mode = "CFB"
    plaintext_string = "Testing AES encrypt and decrypt."
    ciphertext_string = MyAes.encrypt(key, plaintext_string, mode)
    decryptedtext_string = MyAes.decrypt(key, ciphertext_string, mode)
    print("mode: " + mode)
    print("plaintext: " + plaintext_string)
    print("ciphertext: " + ciphertext_string)
    print("decryptedtext: " + decryptedtext_string)
    print("")

    key = MyAes.get_random_key(random.choice(key_sizes))
    mode = "OFB"
    plaintext_string = "Testing AES encrypt and decrypt."
    ciphertext_string = MyAes.encrypt(key, plaintext_string, mode)
    decryptedtext_string = MyAes.decrypt(key, ciphertext_string, mode)
    print("mode: " + mode)
    print("plaintext: " + plaintext_string)
    print("ciphertext: " + ciphertext_string)
    print("decryptedtext: " + decryptedtext_string)
    print("")
    return


if __name__ == "__main__":
    run_test()
