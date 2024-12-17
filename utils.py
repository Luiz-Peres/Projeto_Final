import hashlib
import os
from cryptography.fernet import Fernet

def gerar_chave():
    chave = Fernet.generate_key()
    with open("chave.txt", "wb") as f:
        f.write(chave)

def criptografar(arquivo):
    # Lê a chave secreta do arquivo chave.txt
    with open("chave.txt", "rb") as f:
        chave = f.read()

    # Cria um objeto Fernet com a chave secreta
    fernet = Fernet(chave)

    # Lê o diretório a ser criptografado
    for raiz, dirs, arquivos in os.walk(arquivo):
        for arquivo in arquivos:
            # Criptografa o arquivo
            with open(os.path.join(raiz, arquivo), "rb") as f:
                dados = f.read()
            dados_criptografados = fernet.encrypt(dados)

            # Salva os dados criptografados em um novo arquivo
            with open(os.path.join(raiz, arquivo) + ".cript", "wb") as f:
                f.write(dados_criptografados)

            # Deleta o arquivo original
            os.remove(os.path.join(raiz, arquivo))

def descriptografar(arquivo):
    # Lê a chave secreta do arquivo chave.txt
    with open("chave.txt", "rb") as f:
        chave = f.read()

    # Cria um objeto Fernet com a chave secreta
    fernet = Fernet(chave)

    # Lê o diretório a ser descriptografado
    for raiz, dirs, arquivos in os.walk(arquivo):
        for arquivo in arquivos:
            # Descriptografa o arquivo
            if arquivo.endswith(".cript"):
                with open(os.path.join(raiz, arquivo), "rb") as f:
                    dados_criptografados = f.read()
                dados_descriptografados = fernet.decrypt(dados_criptografados)

                # Salva os dados descriptografados em um novo arquivo
                with open(os.path.join(raiz, arquivo[:-6]), "wb") as f:
                    f.write(dados_descriptografados)

                # Deleta o arquivo criptografado
                os.remove(os.path.join(raiz, arquivo))