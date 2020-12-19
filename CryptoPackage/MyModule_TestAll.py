# 190312k, Dylan Liew, DSF1901
__mydoc__ = """
--------------------------------------------------------------
MyModule_TestAll.py, DylanL
Tested with PyCharm Community Edition 2019.3 x64, python 3.7
--------------------------------------------------------------
"""

from CryptoPackage import MyCaesarCipher_Test
from CryptoPackage import MyAes_Test
from CryptoPackage import MyMonoAlphabetCipher_Test
from CryptoPackage import MyRailFenceTechnique_Test
from CryptoPackage import MySimpleColumnarTranspositionCipher_Test
from CryptoPackage import MyVernamCipher_Test
from CryptoPackage import MyDiffieHellmanKeyExchange_Test
from CryptoPackage import MyDes_Test
def run_test():
    print(__mydoc__)

    MyCaesarCipher_Test.run_test()
    MyMonoAlphabetCipher_Test.run_test()
    MyRailFenceTechnique_Test.run_test()
    MySimpleColumnarTranspositionCipher_Test.run_test()
    MyVernamCipher_Test.run_test()
    MyDiffieHellmanKeyExchange_Test.run_test()
    MyAes_Test.run_test()
    MyDes_Test.run_test()

    return

if __name__ == "__main__":
    run_test()
