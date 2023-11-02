import tkinter as tk
from logic import Logic
from settings import *


class App(tk.Tk):
    def __init__(self, width: int, height: int, title: str, icon_path: str):
        super().__init__()
        self.title(title)
        self.geometry(f"{width}x{height}")
        self.iconbitmap(icon_path)
        self.app_logic = Logic(self)
        self.resizable(True, False)

    def run(self):
        self.mainloop()


if __name__ == "__main__":
    app = App(WIDTH, HEIGHT, TITLE, ICON)
    app.run()
