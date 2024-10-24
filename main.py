import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageGrab
import pytesseract
from deep_translator import GoogleTranslator

pytesseract.pytesseract.tesseract_cmd = r'/Tesseract-OCR/tesseract.exe'

class TradutorImagemApp:
    def __init__(self, master):
        self.master = master
        self.master.title("App de Tradução de Imagens")
        self.master.geometry("500x600")
        self.master.config(bg="#2C3E50")

        # Painel para exibir a imagem carregada
        self.painel_imagem = tk.Label(master, bg="#2C3E50")
        self.painel_imagem.pack(pady=10)

        # Label para exibir a tradução
        self.resultado_traducao = tk.Label(master, text="", wraplength=400, justify="left", font=("Arial", 12), bg="#ECF0F1", relief="sunken", borderwidth=2)
        self.resultado_traducao.pack(pady=20, padx=10)

        # Frame para os botões
        self.frame_botoes = tk.Frame(master, bg="#2C3E50")
        self.frame_botoes.pack(pady=10)

        # Botão para carregar imagem
        botao_carregar = tk.Button(self.frame_botoes, text="Carregar Imagem", command=self.abrir_imagem, bg="#3498DB", fg="white", font=("Arial", 10))
        botao_carregar.grid(row=0, column=0, padx=5)

        # Botão para traduzir a imagem
        botao_traduzir = tk.Button(self.frame_botoes, text="Traduzir Imagem", command=self.traduzir_imagem, bg="#2ECC71", fg="white", font=("Arial", 10))
        botao_traduzir.grid(row=0, column=1, padx=5)

        # Variável para armazenar a imagem atual
        self.imagem_atual = None

        # Bind do atalho CTRL + V
        self.master.bind('<Control-v>', self.atalho_colar)
        # Bind do atalho CTRL + Z para limpar a tela
        self.master.bind('<Control-z>', self.limpar_tela)

    def abrir_imagem(self):
        caminho_imagem = filedialog.askopenfilename()
        if caminho_imagem:
            self.processar_imagem(caminho_imagem)

    def colar_imagem(self):
        imagem = ImageGrab.grabclipboard()
        if isinstance(imagem, Image.Image):
            self.processar_imagem(imagem)
        else:
            messagebox.showerror("Erro", "Nenhuma imagem disponível na área de transferência.")

    def processar_imagem(self, imagem):
        if isinstance(imagem, str):
            imagem = Image.open(imagem)
        imagem = imagem.convert("RGB")
        imagem.thumbnail((400, 400))
        img_exibida = ImageTk.PhotoImage(imagem)
        self.painel_imagem.config(image=img_exibida)
        self.painel_imagem.image = img_exibida
        self.imagem_atual = imagem

    def traduzir_imagem(self):
        if self.imagem_atual is not None:
            texto_extraido = self.extrair_texto(self.imagem_atual)
            if texto_extraido:
                texto_traduzido = self.traduzir_texto(texto_extraido)
                self.resultado_traducao.config(text=f"Texto Traduzido:\n{texto_traduzido}")
            else:
                self.resultado_traducao.config(text="Nenhum texto foi extraído da imagem.")
        else:
            messagebox.showwarning("Aviso", "Por favor, carregue ou cole uma imagem primeiro.")

    def extrair_texto(self, imagem):
        texto = pytesseract.image_to_string(imagem)
        return texto.strip()

    def traduzir_texto(self, texto):
        try:
            traducao = GoogleTranslator(source='auto', target='pt').translate(texto)
            return traducao
        except Exception as e:
            messagebox.showerror("Erro", f"Erro na tradução: {e}")
            return "Erro na tradução"

    def atalho_colar(self, event):
        self.colar_imagem()

    def limpar_tela(self, event):
        self.painel_imagem.config(image=None)
        self.painel_imagem.image = None
        self.imagem_atual = None
        self.resultado_traducao.config(text="")

# Configuração da janela
if __name__ == "__main__":
    root = tk.Tk()
    app = TradutorImagemApp(root)
    root.mainloop()