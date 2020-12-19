# 190312k, Dylan Liew, DSF1901

from CryptoPackage import MyDiffieHellmanKeyExchange

# n and g are prime numbers
n = 11
g = 7


x = 3
y = 6


def run_test():
    print("===== Diffie-Hellman Key Exchange Testing =====")
    result = MyDiffieHellmanKeyExchange.cal_key(n,g,x,y)
    A, B, Key1, Key2 = result[0], result[1], result[2], result[3]
    print("A =", A, "\n"
          "B =", B, "\n"
          "Key1 =", Key1, "\n"
          "Key2 =", Key2)

    return


if __name__ == "__main__":
    run_test()
