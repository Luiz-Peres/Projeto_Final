import tkinter as tk
from tkinter import filedialog
import utils

class CriptografiaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Criptografia de Arquivos")
        self.root.geometry("400x200")

        # Cria os widgets
        self.label_arquivo = tk.Label(root, text="Selecione o arquivo ou pasta:")
        self.label_arquivo.pack()

        self.entry_arquivo = tk.Entry(root, width=50)
        self.entry_arquivo.pack()

        self.botao_selecionar = tk.Button(root, text="Selecionar", command=self.selecionar_arquivo)
        self.botao_selecionar.pack(pady=10)

        self.botao_criptografar = tk.Button(root, text="Criptografar", command=self.criptografar)
        self.botao_criptografar.pack(pady=10)

        self.botao_descriptografar = tk.Button(root, text="Descriptografar", command=self.descriptografar)
        self.botao_descriptografar.pack(pady=10)

        # Configura o tamanho dos botões
        for widget in [self.botao_selecionar, self.botao_criptografar, self.botao_descriptografar]:
            widget.config(width=20, height=2)

    def selecionar_arquivo(self):
        # Abre o diálogo para selecionar o arquivo ou pasta
        pasta = filedialog.askdirectory()
        self.entry_arquivo.delete(0, tk.END)
        self.entry_arquivo.insert(0, pasta)

    def criptografar(self):
        # Gera a chave secreta automaticamente
        utils.gerar_chave()
        # Chama a função de criptografia
        utils.criptografar(self.entry_arquivo.get())

    def descriptografar(self):
        # Chama a função de descriptografia
        utils.descriptografar(self.entry_arquivo.get())

if __name__ == "__main__":
    root = tk.Tk()
    app = CriptografiaApp(root)
    root.mainloop()