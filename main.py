import os
import shutil
from shutil import copyfile
from rsa_functions import newkeys


# os.getcwd() retorna path do diretorio atual
# os.getcwdb() igual mas binario
# os.mkdir(path)
# os.makedirs(path) cria subdiretorios tambem
# OSError
# os.rmdir(path) só remove se o diretorio estiver vazio
# shutil.rmtree() do  modulo shutil deve resolver pra apagar uma pasta toda

c_path = 'private_conversation/'
s_path = 'private_conversation/sender/'
r_path = 'private_conversation/receiver/'


def touch_file(path, info):
    with open(path, "wb+") as infile:
        infile.write(info)


def initialize_conversation():
    try:
        shutil.rmtree(c_path)
    except FileNotFoundError:
        pass

    os.makedirs(s_path)
    os.makedirs(r_path)

    s_public, s_private = newkeys(2048)
    r_public, r_private = newkeys(2048)
    touch_file(s_path + 'public_sender_key.pem', s_public.exportKey('PEM'))
    touch_file(r_path + 'public_sender_key.pem', s_public.exportKey('PEM'))
    touch_file(s_path + 'private_sender_key.pem', s_private.exportKey('PEM'))

    touch_file(r_path + 'public_receiver_key.pem', r_public.exportKey('PEM'))
    touch_file(s_path + 'public_receiver_key.pem', r_public.exportKey('PEM'))
    touch_file(r_path + 'private_receiver_key.pem', r_private.exportKey('PEM'))
    copyfile("chat_files/sender.py", "private_conversation/sender/sender.py")
    copyfile("chat_files/receiver.py", "private_conversation/receiver/receiver.py")

    print("\nAgora ative o ambinte virtual com 'source venv/bin/activate'")
    print("\nApós o ambiente estar ativado, entre na pasta private_conversation/sender, inicie o console do "
          "python3 e importe o sender, siga as instruções e envie uma mensagem.")
    print("Ela será recebida na pasta private_conversation/receiver/\n")
    print("Você deve iniciar o console do python3 na pasta do receiver e importar o módeulo, assim como antes.\n")


if __name__ == "__main__":
    initialize_conversation()
