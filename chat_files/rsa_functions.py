# RSA helper class for pycrypto
# Copyright (c) Dennis Lee
# Date 21 Mar 2017

# Description:
# Python helper class to perform RSA encryption, decryption,
# signing, verifying signatures & keys generation

# Dependencies Packages:
# pycrypto

# Documentation:
# https://www.dlitz.net/software/pycrypto/api/2.6/
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA512, SHA384, SHA256, SHA, MD5
from Crypto import Random
from base64 import b64encode, b64decode

m_hash = "SHA-256"


def newkeys(keysize):
    random_generator = Random.new().read
    key = RSA.generate(keysize, random_generator)
    private, public = key, key.publickey()
    return public, private


def import_key(extern_key):
    return RSA.importKey(extern_key)


def getpublickey(priv_key):
    return priv_key.publickey()


def encrypt(message, pub_key):
    # RSA encryption protocol according to PKCS#1 OAEP
    cipher = PKCS1_OAEP.new(pub_key)
    return cipher.encrypt(message)


def decrypt(ciphertext, priv_key):
    # RSA encryption protocol according to PKCS#1 OAEP
    cipher = PKCS1_OAEP.new(priv_key)
    return cipher.decrypt(ciphertext)


def sign(message, priv_key, hash_alg="SHA-256"):
    global m_hash 
    m_hash = hash_alg
    signer = PKCS1_v1_5.new(priv_key)
    if m_hash == "SHA-512":
        digest = SHA512.new()
    elif m_hash == "SHA-384":
        digest = SHA384.new()
    elif m_hash == "SHA-256":
        digest = SHA256.new()
    elif m_hash == "SHA-1":
        digest = SHA.new()
    else:
        digest = MD5.new()
    digest.update(message)
    print("esse eh o hash: " + str(digest.hexdigest()))
    return signer.sign(digest)


def verify(message, signature, pub_key):
    signer = PKCS1_v1_5.new(pub_key)
    if m_hash == "SHA-512":
        digest = SHA512.new()
    elif m_hash == "SHA-384":
        digest = SHA384.new()
    elif m_hash == "SHA-256":
        digest = SHA256.new()
    elif m_hash == "SHA-1":
        digest = SHA.new()
    else:
        digest = MD5.new()
    digest.update(message)
    return signer.verify(digest, signature)


def main():
    msg2 = b"Hello Tony, I am Jarvis!"
    msg1 = b"Hello Toni, I am Jarvis!"

    keysize = 2048

    (public, private) = newkeys(keysize)

    # https://docs.python.org/3/library/base64.html
    # encodes the bytes-like object s
    # returns bytes
    encrypted = b64encode(encrypt(msg1, private))
    # decodes the Base64 encoded bytes-like object or ASCII string s
    # returns the decoded bytes
    decrypted = decrypt(b64decode(encrypted), private)
    signature = b64encode(sign(msg1, private, "SHA-512"))

    _verify = verify(msg1, b64decode(signature), public)

    # print(private.exportKey('PEM'))
    # print(public.exportKey('PEM'))
    print("Encrypted: " + encrypted.decode('ascii'))
    print("Decrypted: '%s'" % decrypted)
    print("Signature: " + signature.decode('ascii'))
    print("Verify: %s" % _verify)
    verify(msg2, b64decode(signature), public)


if __name__ == "__main__":
    main()
