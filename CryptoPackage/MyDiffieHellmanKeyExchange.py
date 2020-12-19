# 190312k, Dylan Liew, DSF1901


def cal_key(n, g, x, y):
    A = (g**x) % n
    B = (g**y) % n
    Key1 = (B**x) % n
    Key2 = (A**y) % n
    return [A, B, Key1, Key2]
