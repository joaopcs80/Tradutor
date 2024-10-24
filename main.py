import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import pytesseract
import googletrans

class TradutorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Tradutor de Imagens")

        self.label = tk.Label(master, text="Pressione 'S' para selecionar a área")
        self.label.pack()

        self.canvas = tk.Canvas(master, bg='white')
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.canvas.bind("<ButtonPress-1>", self.start_selection)
        self.canvas.bind("<B1-Motion>", self.update_selection)
        self.canvas.bind("<ButtonRelease-1>", self.end_selection)
        self.master.bind("<s>", self.activate_selection_mode)

        self.image = None
        self.rect = None
        self.start_x = None
        self.start_y = None

    def activate_selection_mode(self, event):
        self.label.config(text="Selecione a área com o mouse")
        self.canvas.bind("<ButtonPress-1>", self.start_selection)

    def start_selection(self, event):
        self.start_x = event.x
        self.start_y = event.y
        self.rect = self.canvas.create_rectangle(self.start_x, self.start_y, self.start_x, self.start_y, outline='red')

    def update_selection(self, event):
        self.canvas.coords(self.rect, self.start_x, self.start_y, event.x, event.y)

    def end_selection(self, event):
        end_x, end_y = event.x, event.y
        self.canvas.unbind("<ButtonPress-1>")
        self.extract_text_from_selection(self.start_x, self.start_y, end_x, end_y)

    def load_image(self, file_path):
        self.image = Image.open(file_path)
        self.image.thumbnail((800, 600))  # Reduz o tamanho da imagem
        self.photo = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)

    def extract_text_from_selection(self, x1, y1, x2, y2):
        cropped_image = self.image.crop((x1, y1, x2, y2))
        text = pytesseract.image_to_string(cropped_image)

        translator = googletrans.Translator()
        translation = translator.translate(text, dest='pt').text

        self.label.config(text=f'Texto: {text}\nTradução: {translation}')

if __name__ == "__main__":
    root = tk.Tk()
    app = TradutorApp(root)
    app.load_image('caminho_para_sua_imagem.png')  # Altere para o caminho da sua imagem
    root.mainloop()