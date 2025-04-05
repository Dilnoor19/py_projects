import tkinter as tk
from tkinter import ttk

class ModernCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Modern Calculator")
        self.root.geometry("400x550")
        self.root.configure(bg="#2d2d2d")
        self.root.resizable(False, False)

        self.expression = ""
        self.input_var = tk.StringVar()

        self.main_font = ("Segoe UI", 20, "bold")
        self.symbol_font = ("Segoe UI", 24, "bold")

        self.entry_frame = tk.Frame(root, bg="#2d2d2d")
        self.entry_frame.pack(padx=10, pady=20, fill="x")
        
        self.entry = tk.Entry(self.entry_frame, textvariable=self.input_var, font=self.symbol_font,
                              bg="#3d3d3d", fg="white", justify="right", bd=0, relief="flat",
                              insertbackground="white", highlightthickness=2,
                              highlightcolor="#4d4d4d", highlightbackground="#3d3d3d")
        self.entry.pack(fill="x", ipady=12)

        self.buttons_frame = tk.Frame(root, bg="#2d2d2d")
        self.buttons_frame.pack(padx=10, pady=10, fill="both", expand=True)

        self.buttons_frame.columnconfigure([0, 1, 2, 3], weight=1, uniform="btn")
        self.buttons_frame.rowconfigure([0, 1, 2, 3, 4], weight=1, uniform="btn")

        self.create_buttons()
        self.root.bind("<Key>", self.key_input)

    def create_buttons(self):
        buttons = [
            ("C", "CE", "%", "÷"),
            ("7", "8", "9", "×"),
            ("4", "5", "6", "-"),
            ("1", "2", "3", "+"),
            ("0", ".", "⌫", "=")
        ]

        for row_idx, row in enumerate(buttons):
            for col_idx, text in enumerate(row):
                self.create_button(row_idx, col_idx, text)

    def create_button(self, row, col, text):
        bg_color = "#3d3d3d"
        fg_color = "white"
        hover_color = "#4d4d4d"
        
        if text in ("÷", "×", "-", "+", "="):
            bg_color = "#ff9500"
            hover_color = "#ffaa00"
        elif text in ("C", "CE"):
            bg_color = "#ff4c4c"
            hover_color = "#ff6666"
        elif text == "=":
            bg_color = "#007acc"
            hover_color = "#0088e6"
        
        btn = tk.Button(
            self.buttons_frame, text=text, font=self.main_font,
            bg=bg_color, fg=fg_color, relief="flat", bd=0,
            activebackground=hover_color, activeforeground=fg_color,
            highlightthickness=1, highlightbackground="#4d4d4d",
            command=lambda t=text: self.on_button_click(t)
        )
        
        if text == "0":
            btn.grid(row=row, column=col, columnspan=2, sticky="nsew", padx=2, pady=2)
        else:
            btn.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)
        
        btn.bind("<Enter>", lambda e, b=btn, h=hover_color: b.config(bg=h))
        btn.bind("<Leave>", lambda e, b=btn, c=bg_color: b.config(bg=c))

    def on_button_click(self, char):
        operators = {"÷": "/", "×": "*", "⌫": "←"}
        char = operators.get(char, char)
        
        if char == "C":
            self.expression = ""
        elif char == "←":
            self.expression = self.expression[:-1]
        elif char == "=":
            try:
                self.expression = str(eval(self.expression))
            except:
                self.expression = "Error"
        else:
            self.expression += char
        
        self.input_var.set(self.expression)

    def key_input(self, event):
        key = event.char
        if key in "0123456789+-*/.=":
            self.on_button_click(key)
        elif key == "\r":
            self.on_button_click("=")
        elif key == "\x08":
            self.on_button_click("←")

if __name__ == "__main__":
    root = tk.Tk()
    app = ModernCalculator(root)
    root.mainloop()
