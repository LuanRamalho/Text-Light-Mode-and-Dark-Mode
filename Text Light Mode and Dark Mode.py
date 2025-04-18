import tkinter as tk
from tkinter import ttk

class LightDarkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Light Mode - Dark Mode")
        self.root.geometry("800x600")
        self.root.configure(bg="white")

        self.is_dark = False

        # Estilo geral do texto
        self.text_style = {
            "font": ("Work Sans", 11),
            "wraplength": 760,
            "justify": "left",
            "bg": "white",
            "fg": "black",
            "anchor": "nw"
        }

        # Frame principal
        self.container = tk.Frame(self.root, height=50, bg="white")
        self.container.pack(fill="x", pady=(20, 10), padx=20)

        # Botão de toggle (modo claro/escuro)
        self.toggle_button = tk.Canvas(self.container, width=75, height=40, bg="white", highlightthickness=0)
        self.toggle_bg = self.toggle_button.create_oval(0, 0, 75, 40, fill="black", outline="")  # Início: modo claro
        self.toggle_circle = self.toggle_button.create_oval(5, 5, 35, 35, fill="white", outline="")  # círculo à esquerda

        self.toggle_button.bind("<Button-1>", self.toggle_theme)
        self.toggle_button.pack(side="right")

        # Texto (Lorem Ipsum)
        self.text_label = tk.Label(
            self.root,
            text=("Lorem ipsum dolor sit amet consectetur adipisicing elit. Facilis, ab sequi! "
                  "Ipsum, reprehenderit! Dolor vero sunt corporis ea natus, nulla cum assumenda. "
                  "Nostrum corporis molestiae corrupti magni..." * 3),
            **self.text_style
        )
        self.text_label.pack(fill="both", expand=True, padx=30, pady=10)

    def toggle_theme(self, event=None):
        self.is_dark = not self.is_dark
        if self.is_dark:
            # Modo escuro
            self.root.configure(bg="#15181f")
            self.container.configure(bg="#15181f")
            self.toggle_button.configure(bg="#15181f")
            self.toggle_button.itemconfig(self.toggle_bg, fill="white")  # fundo branco
            self.toggle_button.itemconfig(self.toggle_circle, fill="black")  # círculo preto
            self.toggle_button.coords(self.toggle_circle, 35, 5, 65, 35)  # círculo à direita
            self.text_label.configure(bg="#15181f", fg="#e5e5e5")
        else:
            # Modo claro
            self.root.configure(bg="white")
            self.container.configure(bg="white")
            self.toggle_button.configure(bg="white")
            self.toggle_button.itemconfig(self.toggle_bg, fill="black")  # fundo preto
            self.toggle_button.itemconfig(self.toggle_circle, fill="white")  # círculo branco
            self.toggle_button.coords(self.toggle_circle, 5, 5, 35, 35)  # círculo à esquerda
            self.text_label.configure(bg="white", fg="black")


# Executar o app
if __name__ == "__main__":
    root = tk.Tk()
    app = LightDarkApp(root)
    root.mainloop()
