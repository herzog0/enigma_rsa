from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
from base64 import b64encode
from termcolor import colored
import random


def _import_key(path):
    with open(path) as key:
        key_s = key.read()
    return RSA.importKey(key_s)


public_s = _import_key("public_sender_key.pem")
private_s = _import_key("private_sender_key.pem")
public_r = _import_key("public_receiver_key.pem")


print(colored("\nCopie e cole a linha a seguir: ", "magenta"))
print("from sender import encrypt, get_hash, get_sign, send, helpme, public_s, private_s, public_r\n")
print("Após isso, use o comando helpme() para obter ajuda sobre a sua função de " + colored("sender\n", "red"))


def helpme():
    print("")
    print(colored("Você é ", "red") + colored("sender", "yellow"))
    print(colored("Você pode usar as funções: ", "red"))
    print(colored("encrypt(<msg>, <pub_key>)", "cyan") + " -> encripta uma mensagem com a chave pública")
    print(colored("get_hash(<msg>)", "cyan") + " -> retorna um hash da mensagem")
    print(colored("get_sign(<hash>, <priv_key>)", "cyan") + " -> gera a assinatura a partir do hash e chave privada")
    print(colored("send(<msg>, opt: <sign>)", "cyan") + " -> envia a mensagem e, opcionalmente, uma assinatura")
    print(colored("public_s", "cyan") + " -> sua chave pública")
    print(colored("private_s", "cyan") + " -> sua chave privada")
    print(colored("public_r", "cyan") + " -> a chave pública do receiver")
    print("")


# def _ls():
#     onlyfiles = [f for f in listdir("./") if isfile(join("./", f))]
#     for file in onlyfiles:
#         if file == "sender.py":
#             continue
#         print(file)


def send(encrypted_msg, sign=None):
    new_msg = mitm(sign)
    with open("../receiver/message.txt", "wb+") as msg:
        if new_msg:
            msg.write(new_msg)
        else:
            msg.write(encrypted_msg)
    if sign:
        with open("../receiver/signature.txt", "wb+") as signa:
            signa.write(sign)


def encrypt(message, pub_key):
    # RSA encryption protocol according to PKCS#1 OAEP
    if isinstance(message, str):
        message = str.encode(message)
    cipher = PKCS1_OAEP.new(pub_key)
    return b64encode(cipher.encrypt(message))


def get_hash(message):
    try:
        message = str.encode(message)
    except TypeError:
        pass
    digest = SHA256.new()
    digest.update(message)
    print(colored("\nHash da mensagem: ", "green") + str(b64encode(digest.digest())) + "\n")
    return digest


def get_sign(m_hash, priv_key):
    signer = PKCS1_v1_5.new(priv_key)
    ass = signer.sign(m_hash)
    print(colored("\nAssinatura: ", "red") + str(b64encode(ass)) + "\n")
    return b64encode(ass)


def mitm(sign=None):
    if not sign:
        return encrypt("Oi querid, me passa os dados do seu cartão de crédito rapidinho?", public_r)
    else:
        chance = random.randint(1, 10)
        if chance <= 6:
            return encrypt("Oi querid, me passa os dados do seu cartão de crédito rapidinho?", public_r)
        return None


# def main():
#     public, private = newkeys(2048)
#     msg = ""
#     while True:
#         if not msg:
#             pass
#         else:
#             msg = str.encode(msg)
#             h = hash(msg)
#             ass = sign(h, private)
#             print(colored("Assinatura: ", "red") + str(b64encode(ass)))
#         msg = input(colored(":>>>>  ", "green"))


# if __name__ == '__main__':
#     main()
