import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageGrab
import pytesseract
from googletrans import Translator

# Função para abrir a imagem
def abrir_imagem():
    caminho_imagem = filedialog.askopenfilename()
    if caminho_imagem:
        processar_imagem(caminho_imagem)

# Função para processar a imagem
def processar_imagem(caminho_imagem):
    imagem = Image.open(caminho_imagem)
    imagem.thumbnail((400, 400))
    img_exibida = ImageTk.PhotoImage(imagem)
    painel_imagem.config(image=img_exibida)
    painel_imagem.image = img_exibida
    texto_extraido = extrair_texto(caminho_imagem)
    texto_traduzido = traduzir_texto(texto_extraido)
    resultado_traducao.config(text=f"Texto Traduzido:\n{texto_traduzido}")

# Função para extrair texto da imagem
def extrair_texto(caminho_imagem):
    imagem = Image.open(caminho_imagem)
    texto = pytesseract.image_to_string(imagem)
    return texto

# Função para traduzir o texto para português
def traduzir_texto(texto):
    tradutor = Translator()
    traducao = tradutor.translate(texto, dest='pt')
    return traducao.text

# Função para colar imagem da área de transferência
def colar_imagem():
    imagem = ImageGrab.grabclipboard()
    if isinstance(imagem, Image.Image):  # Verifica se a imagem foi obtida
        processar_imagem(imagem)
    else:
        resultado_traducao.config(text="Nenhuma imagem disponível na área de transferência.")

# Configuração da janela principal
janela = tk.Tk()
janela.title("App de Tradução de Imagens")
janela.geometry("500x600")

# Botão para carregar imagem
botao_carregar = tk.Button(janela, text="Carregar Imagem", command=abrir_imagem)
botao_carregar.pack(pady=10)

# Botão para colar imagem da área de transferência
botao_colar = tk.Button(janela, text="Colar Imagem (CTRL+V)", command=colar_imagem)
botao_colar.pack(pady=10)

# Painel para exibir a imagem carregada
painel_imagem = tk.Label(janela)
painel_imagem.pack()

# Label para exibir a tradução
resultado_traducao = tk.Label(janela, text="", wraplength=400, justify="left")
resultado_traducao.pack(pady=20)

# Inicia o loop da interface gráfica
janela.mainloop()