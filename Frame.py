import tkinter as tk
from tkinter import font

root = tk.Tk()
root.title("Analytic Desktop App")
root.geometry("800x600")
root.configure(bg="white")

title_font = font.Font(family="Helvetica", size=32, weight="bold")
ui_font = font.Font(family="Helvetica", size=14)

# Title text (replaces Hello World)
title = tk.Label(root, text="Análise de Dados", font=title_font, bg="white", fg="#111")
title.pack(pady=(30, 10))

# "Box" that will contain the 3 button rows
box = tk.Frame(root, bg="white", bd=1, relief="solid")
box.pack(padx=40, pady=20, fill="x")

# Center the content inside the box
box.grid_columnconfigure(0, weight=1)  # left spacer
box.grid_columnconfigure(1, weight=0)  # labels
box.grid_columnconfigure(2, weight=0)  # buttons
box.grid_columnconfigure(3, weight=1)  # right spacer



BUTTON_WIDTH = 18  # same width for all buttons

def make_row(row, name_text, button_text, command):
    name = tk.Label(box, text=name_text, font=ui_font, bg="white", fg="#111")
    btn = tk.Button(box, text=button_text, font=ui_font, width=BUTTON_WIDTH, bg="#1e88e5", fg="white",
                    activebackground="#1565c0", activeforeground="white",
                    relief="flat", padx=16, pady=6, command=command)

    name.grid(row=row, column=1, padx=(20, 12), pady=12, sticky="e")
    btn.grid(row=row, column=2, padx=(12, 20), pady=12, sticky="w")

# 3 rows (first one as you requested)
make_row(0, "Gerar Análise",     "Iniciar",          lambda: print("Gerar Análise"))
make_row(1, "Atualizar Dados",   "Atualizar",        lambda: print("Atualizar Dados"))
make_row(2, "Upload de Arquivos","Selecionar arquivo", lambda: print("Upload de Arquivos"))

root.mainloop()