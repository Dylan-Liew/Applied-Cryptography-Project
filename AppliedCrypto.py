from flask import request, Flask, render_template, jsonify
from CryptoPackage import \
    MyCaesarCipher,\
    MyMonoAlphabetCipher,\
    MyRailFenceTechnique,\
    MySimpleColumnarTranspositionCipher,\
    MyVernamCipher,\
    MyDiffieHellmanKeyExchange,\
    MyAes,\
    MyDes

# Flask

app = Flask(__name__)

# Need For InfoSecurity
@app.route('/')
def home():
    return render_template('pages/home.html')

# Cryptography Concepts & Techniques
# Shift Cipher
@app.route("/ShiftCipher/")
def ShiftCipher():
    return render_template('pages/shift_cipher.html')


@app.route("/api/ShiftCipher/", methods=["POST"])
def apiShiftCipher():
    data = request.get_json()
    operation = data["type"]
    text = data["text"]
    key = int(data["key"])
    if operation == "encrypt":
        cipher_text = MyCaesarCipher.encrypt(key, text)
        return jsonify({"cipher_text": cipher_text})
    else:
        plain_text = MyCaesarCipher.decrypt(key, text)
        return jsonify({"plain_text": plain_text})

# Mono-Alphabet Cipher
@app.route("/MonoAlphabetCipher/")
def MonoAlphabetCipher():
    return render_template('pages/mono_alphabet_cipher.html')


@app.route("/api/MonoAlphabetCipher/", methods=["POST"])
def apiMonoAlphabetCipher():
    data = request.get_json()
    operation = data["type"]
    text = data["text"]
    key = data["key"]
    if operation == "encrypt":
        cipher_text = MyMonoAlphabetCipher.encrypt(text, key)
        return jsonify({"cipher_text": cipher_text})
    else:
        plain_text = MyMonoAlphabetCipher.decrypt(text, key)
        return jsonify({"plain_text": plain_text})

# Rail Fence Cipher
@app.route("/RailFenceTechnique/")
def RailFenceTechnique():
    return render_template('pages/rail_fence_technique.html')


@app.route("/api/RailFenceTechnique/", methods=["POST"])
def apiRailFenceTechnique():
    data = request.get_json()
    operation = data["type"]
    text = data["text"]
    key = int(data["key"])
    if operation == "encrypt":
        cipher_text = MyRailFenceTechnique.encrypt(text, key)
        return jsonify({"cipher_text": cipher_text})
    else:
        plain_text = MyRailFenceTechnique.decrypt(text, key)
        return jsonify({"plain_text": plain_text})

# Simple Columnar Transposition Technique
@app.route("/SimpleColumnarTranspositionTechnique/")
def SimpleColumnarTranspositionTechnique():
    return render_template('pages/simple_columnar_transposition_technique.html')


@app.route("/api/SimpleColumnarTranspositionTechnique/", methods=["POST"])
def apiSimpleColumnarTranspositionTechnique():
    data = request.get_json()
    operation = data["type"]
    text = data["text"]
    key = int(data["key"])
    if operation == "encrypt":
        cipher_text = MySimpleColumnarTranspositionCipher.encrypt(text, key)
        return jsonify({"cipher_text": cipher_text})
    else:
        plain_text = MySimpleColumnarTranspositionCipher.decrypt(text, key)
        return jsonify({"plain_text": plain_text})

# Vernam Cipher
@app.route("/VernamCipher/")
def VernamCipher():
    return render_template('pages/vernam_cipher.html')


@app.route("/api/VernamCipher/", methods=["POST"])
def apiVernamCipher():
    data = request.get_json()
    operation = data["type"]
    text = data["text"]
    key = data["key"]
    if operation == "encrypt":
        cipher_text = MyVernamCipher.encrypt(text, key)
        return jsonify({"cipher_text": cipher_text})
    else:
        plain_text = MyVernamCipher.decrypt(text, key)
        return jsonify({"plain_text": plain_text})

# Diffie-Hellman Key Exchange
@app.route("/DiffieHellmanKeyExchange/")
def DiffieHellmanKeyExchange():
    return render_template('pages/diffie_hellman_key_exchange.html')


@app.route("/api/DiffieHellmanKeyExchange/", methods=["POST"])
def apiDiffieHellmanKeyExchange():
    data = request.get_json()
    n = int(data["n"])
    g = int(data["g"])
    x = int(data["x"])
    y = int(data["y"])
    output = MyDiffieHellmanKeyExchange.cal_key(n, g, x, y)
    A = output[0]
    B = output[1]
    Key1 = output[2]
    Key2 = output[3]
    return jsonify({"A": A,"B": B,"Key1": Key1, "Key2": Key2})


# Symmetric Algorithms
# AES
@app.route("/AES/")
def AES():
    return render_template('pages/aes.html')


@app.route("/api/AES/", methods=["POST"])
def apiAES():
    data = request.get_json()
    operation = data["type"]
    text = data["text"]
    mode = data["mode"]
    key = data["key"].encode('utf-8')
    if operation == "encrypt":
        cipher_text = MyAes.encrypt(key, text, mode)
        return jsonify({"cipher_text": cipher_text})
    else:
        plain_text = MyAes.decrypt(key, text, mode)
        return jsonify({"plain_text": plain_text})

# DES
@app.route("/DES/")
def DES():
    return render_template('pages/des.html')


@app.route("/api/DES/", methods=["POST"])
def apiDES():
    data = request.get_json()
    operation = data["type"]
    text = data["text"]
    mode = data["mode"]
    key = data["key"].encode('utf-8')
    if operation == "encrypt":
        cipher_text = MyDes.encrypt(key, text, mode)
        return jsonify({"cipher_text": cipher_text})
    else:
        plain_text = MyDes.decrypt(key, text, mode)
        return jsonify({"plain_text": plain_text})


if __name__ == '__main__':
    app.run(debug=True)
