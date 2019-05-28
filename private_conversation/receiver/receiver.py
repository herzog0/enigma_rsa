from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256

from base64 import b64decode
from termcolor import colored


print(colored("\nCopie e cole a linha a seguir: ", "magenta"))
print("from receiver import get_message, get_signature, decrypt, verify, helpme, public_r, private_r, public_s\n")
print("Após isso, use o comando helpme() para obter ajuda sobre a sua função de " + colored("receiver\n", "red"))


def _import_key(path):
    with open(path) as key:
        key_s = key.read()
    return RSA.importKey(key_s)


public_r = _import_key("public_receiver_key.pem")
private_r = _import_key("private_receiver_key.pem")
public_s = _import_key("public_sender_key.pem")


def get_message():
    message = None
    try:
        with open("message.txt") as msg:
            message = msg.read()
    except FileNotFoundError:
        print(colored("Parece que não há nenhuma mensagem para ser lida!", "red"))
    return message


def get_signature():
    signature = None
    try:
        with open("signature.txt") as sign:
            signature = sign.read()
    except FileNotFoundError:
        print(colored("Parece que não há nenhuma assinatura para ser lida!", "red"))
    return signature


def helpme():
    print("")
    print(colored("Você é ", "red") + colored("receiver", "yellow"))
    print(colored("Você pode usar as funções: ", "red"))
    print(colored("decrypt(<msg>, <priv_key>)", "cyan") + " -> decripta uma mensagem com sua chave privada")
    print(colored("verify(<msg>, <pub_s_key>, <sign>)", "cyan") + " -> "
                                                                  "verifica se a mensagem foi alterada a partir de "
                                                                  "uma assinatura e da chave pública de quem a "
                                                                  "assinou")
    print(colored("get_message()", "cyan") + " -> retorna a mensagem contida na pasta ou nulo")
    print(colored("get_signature()", "cyan") + " -> retorna a assinatura contida na pasta ou nulo")

    print(colored("public_r", "cyan") + " -> sua chave pública")
    print(colored("private_r", "cyan") + " -> sua chave privada")
    print(colored("public_s", "cyan") + " -> a chave pública do sender")
    print("")


def decrypt(ciphertext, priv_key):
    # RSA encryption protocol according to PKCS#1 OAEP
    ciphertext = b64decode(ciphertext)
    cipher = PKCS1_OAEP.new(priv_key)
    ciphertext = cipher.decrypt(ciphertext)
    if isinstance(ciphertext, bytes):
        ciphertext = bytes.decode(ciphertext)
    return ciphertext


def verify(message, pub_key=None, signature=None):
    if isinstance(message, bytes):
        message = bytes.decode(message)
    if not signature:
        print(colored("Impossível verificar a consistência da mensagem! (Não há assinatura)", "red"))
        print("\nMensagem: " + colored(message, "yellow") + "\n")
        return
    signer = PKCS1_v1_5.new(pub_key)
    digest = SHA256.new()
    digest.update(str.encode(message))
    if signer.verify(digest, b64decode(signature)):
        print(colored("A mensagem está intacta!", "green"))
        print("\nMensagem: " + colored(message, "yellow") + "\n")
    else:
        print(colored("Tome cuidado pois a mensagem foi alterada!", "red"))
        print("\nMensagem: " + colored(message, "yellow") + "\n")
