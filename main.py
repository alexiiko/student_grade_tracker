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

    def run(self):
        self.mainloop()

    def update_averages(self):
        self.after(1000, self.update_averages)


if __name__ == "__main__":
    app = App(WIDTH, HEIGHT, TITLE, ICON)
    app.run()
