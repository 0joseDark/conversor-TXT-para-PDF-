Aqui está um **conversor de TXT para PDF** em Python com uma **janela gráfica**, **botões**, **menu**, **caixas de texto** para selecionar pastas e uma **barra de progresso**. Vamos usar **Tkinter** para a interface e **FPDF** para a conversão.  

---

## **📌 Instalação dos módulos necessários**

- pip install fpdf tk

- **fpdf** → Para criar e salvar o PDF.  
- **tk** (Tkinter) → Para criar a interface gráfica.  
## **🖥️ Código Completo**
Este script cria uma janela com:
✅ **Caixas de texto** para selecionar a pasta de entrada e saída.  
✅ **Botão "Converter"** para iniciar a conversão.  
✅ **Botão "Sair"** para fechar o programa.  
✅ **Barra de progresso (%)** mostrando o andamento.  
✅ **Menu "Ficheiro"** com opções para abrir e sair.  

import os
import tkinter as tk
from tkinter import filedialog, messagebox
from fpdf import FPDF
from tkinter import ttk  # Para a barra de progresso

class ConversorTXTparaPDF:
    def __init__(self, root):
        self.root = root
        self.root.title("Conversor TXT para PDF")
        self.root.geometry("500x300")

        # Criar menu
        self.menu_bar = tk.Menu(root)
        self.menu_ficheiro = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_ficheiro.add_command(label="Abrir Pasta", command=self.selecionar_pasta_entrada)
        self.menu_ficheiro.add_command(label="Sair", command=root.quit)
        self.menu_bar.add_cascade(label="Ficheiro", menu=self.menu_ficheiro)
        root.config(menu=self.menu_bar)

        # Caixa de texto para pasta de entrada
        tk.Label(root, text="Pasta de Entrada:").pack()
        self.entrada_txt = tk.Entry(root, width=50)
        self.entrada_txt.pack()
        tk.Button(root, text="Selecionar", command=self.selecionar_pasta_entrada).pack()

        # Caixa de texto para pasta de saída
        tk.Label(root, text="Pasta de Saída:").pack()
        self.saida_pdf = tk.Entry(root, width=50)
        self.saida_pdf.pack()
        tk.Button(root, text="Selecionar", command=self.selecionar_pasta_saida).pack()

        # Barra de Progresso
        self.progresso = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
        self.progresso.pack(pady=10)

        # Botões
        tk.Button(root, text="Converter", command=self.converter_txt_para_pdf).pack(pady=5)
        tk.Button(root, text="Sair", command=root.quit).pack(pady=5)

    def selecionar_pasta_entrada(self):
        pasta = filedialog.askdirectory()
        if pasta:
            self.entrada_txt.delete(0, tk.END)
            self.entrada_txt.insert(0, pasta)

    def selecionar_pasta_saida(self):
        pasta = filedialog.askdirectory()
        if pasta:
            self.saida_pdf.delete(0, tk.END)
            self.saida_pdf.insert(0, pasta)

    def converter_txt_para_pdf(self):
        pasta_entrada = self.entrada_txt.get()
        pasta_saida = self.saida_pdf.get()

        if not os.path.exists(pasta_entrada) or not os.path.exists(pasta_saida):
            messagebox.showerror("Erro", "Selecione pastas válidas!")
            return

        arquivos_txt = [f for f in os.listdir(pasta_entrada) if f.endswith(".txt")]
        
        if not arquivos_txt:
            messagebox.showinfo("Info", "Nenhum arquivo TXT encontrado na pasta de entrada.")
            return

        self.progresso["maximum"] = len(arquivos_txt)
        self.progresso["value"] = 0

        for i, arquivo in enumerate(arquivos_txt, 1):
            caminho_txt = os.path.join(pasta_entrada, arquivo)
            nome_pdf = os.path.splitext(arquivo)[0] + ".pdf"
            caminho_pdf = os.path.join(pasta_saida, nome_pdf)

            self.criar_pdf(caminho_txt, caminho_pdf)
            self.progresso["value"] = i
            self.root.update_idletasks()

        messagebox.showinfo("Sucesso", "Conversão concluída!")

    def criar_pdf(self, txt_path, pdf_path):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        with open(txt_path, "r", encoding="utf-8") as f:
            for linha in f:
                pdf.cell(200, 10, linha.strip(), ln=True)

        pdf.output(pdf_path)

if __name__ == "__main__":
    root = tk.Tk()
    app = ConversorTXTparaPDF(root)
    root.mainloop()
