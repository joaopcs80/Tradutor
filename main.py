import tkinter as tk
from PIL import Image
import pytesseract
from googletrans import Translator
import pyautogui

class TradutorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Tradutor de Captura de Tela")

        self.label = tk.Label(master, text="Selecione a área da tela")
        self.label.pack()

        self.canvas = tk.Canvas(master, bg='white', width=800, height=600)
        self.canvas.pack()

        self.canvas.bind("<ButtonPress-1>", self.start_selection)
        self.canvas.bind("<B1-Motion>", self.update_selection)
        self.canvas.bind("<ButtonRelease-1>", self.end_selection)

        self.rect = None
        self.start_x = None
        self.start_y = None

    def start_selection(self, event):
        self.start_x = event.x
        self.start_y = event.y
        self.rect = self.canvas.create_rectangle(self.start_x, self.start_y, self.start_x, self.start_y, outline='red')

    def update_selection(self, event):
        self.canvas.coords(self.rect, self.start_x, self.start_y, event.x, event.y)

    def end_selection(self, event):
        end_x, end_y = event.x, event.y
        self.capture_and_translate(self.start_x, self.start_y, end_x, end_y)

    def capture_and_translate(self, x1, y1, x2, y2):
        # Captura a área da tela
        screenshot = pyautogui.screenshot(region=(x1, y1, x2 - x1, y2 - y1))

        # Converte a captura para um formato PIL
        cropped_image = Image.fromarray(screenshot)

        # Extrai texto da imagem recortada
        text = pytesseract.image_to_string(cropped_image)

        # Traduz o texto
        translator = Translator()
        try:
            translation = translator.translate(text, dest='pt').text
        except Exception as e:
            translation = f"Erro na tradução: {e}"

        # Atualiza a label com o texto extraído e sua tradução
        self.label.config(text=f'Texto: {text.strip()}\nTradução: {translation.strip()}')

if __name__ == "__main__":
    root = tk.Tk()
    app = TradutorApp(root)
    root.mainloop()