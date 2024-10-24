import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import pytesseract
from googletrans import Translator

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

class TradutorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("App de Tradução de Imagens")
        self.master.geometry("500x600")

        self.botao_carregar = tk.Button(master, text="Carregar Imagem", command=self.abrir_imagem)
        self.botao_carregar.pack(pady=10)

        self.painel_imagem = tk.Label(master)
        self.painel_imagem.pack()

        self.resultado_traducao = tk.Label(master, text="", wraplength=400, justify="left")
        self.resultado_traducao.pack(pady=20)

        self.canvas = tk.Canvas(master, bg='white')
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.image = None
        self.rect = None
        self.start_x = None
        self.start_y = None

        self.canvas.bind("<ButtonPress-1>", self.start_selection)
        self.canvas.bind("<B1-Motion>", self.update_selection)
        self.canvas.bind("<ButtonRelease-1>", self.end_selection)

    def abrir_imagem(self):
        caminho_imagem = filedialog.askopenfilename()
        if caminho_imagem:
            self.image = Image.open(caminho_imagem)
            self.image.thumbnail((400, 400))
            img_exibida = ImageTk.PhotoImage(self.image)
            self.painel_imagem.config(image=img_exibida)
            self.painel_imagem.image = img_exibida
            self.canvas.delete("all")  # Limpa o canvas antes de carregar a nova imagem
            self.canvas.create_image(0, 0, anchor=tk.NW, image=img_exibida)

    def start_selection(self, event):
        self.start_x = event.x
        self.start_y = event.y
        self.rect = self.canvas.create_rectangle(self.start_x, self.start_y, self.start_x, self.start_y, outline='red')

    def update_selection(self, event):
        self.canvas.coords(self.rect, self.start_x, self.start_y, event.x, event.y)

    def end_selection(self, event):
        end_x, end_y = event.x, event.y
        self.extract_text_from_selection(self.start_x, self.start_y, end_x, end_y)

    def extract_text_from_selection(self, x1, y1, x2, y2):
        cropped_image = self.image.crop((x1 * (self.image.width / 400), y1 * (self.image.height / 400),
                                          x2 * (self.image.width / 400), y2 * (self.image.height / 400)))
        texto_extraido = pytesseract.image_to_string(cropped_image)
        texto_traduzido = self.traduzir_texto(texto_extraido)
        self.resultado_traducao.config(text=f"Texto Traduzido:\n{texto_traduzido}")

    def traduzir_texto(self, texto):
        if texto.strip():  # Verifica se o texto não está vazio
            tradutor = Translator()
            traducao = tradutor.translate(texto, dest='pt')
            return traducao.text
        return "Nenhum texto para traduzir."

# Inicializa a aplicação
if __name__ == "__main__":
    root = tk.Tk()
    app = TradutorApp(root)
    root.mainloop()