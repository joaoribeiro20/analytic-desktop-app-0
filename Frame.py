import tkinter as tk
from tkinter import font


# -----------------------------------------------------------------------------
# Constants
# -----------------------------------------------------------------------------

WINDOW_TITLE = "Analytic Desktop App"
WINDOW_SIZE = "800x600"
BG_COLOR = "white"
BUTTON_WIDTH = 18

# -----------------------------------------------------------------------------
# Helper functions
# -----------------------------------------------------------------------------


def show_balloon(parent, message, widget):
    """Show a balloon popup with the message, positioned to the right of the info button."""
    balloon = tk.Toplevel(parent)
    balloon.withdraw()
    balloon.overrideredirect(True)
    balloon.attributes("-topmost", True)

    frame = tk.Frame(balloon, bg="white", bd=1, relief="solid")
    frame.pack(padx=8, pady=8)

    label = tk.Label(
        frame,
        text=message,
        font=("Helvetica", 10),
        bg="white",
        fg="#333",
        wraplength=300,
        justify="left",
    )
    label.pack(padx=12, pady=8)

    def close_balloon(event=None):
        balloon.destroy()

    label.bind("<Button-1>", close_balloon)
    frame.bind("<Button-1>", close_balloon)

    balloon.update_idletasks()
    x = widget.winfo_rootx() + widget.winfo_width() + 8
    y = widget.winfo_rooty() - 10
    balloon.geometry(f"+{x}+{y}")
    balloon.deiconify()


def make_row(parent, box, row, name_text, button_text, command, hint_text, ui_font):
    """Create a row with label, action button, and info button."""
    name = tk.Label(box, text=name_text, font=ui_font, bg="white", fg="#111")
    btn = tk.Button(
        box,
        text=button_text,
        font=ui_font,
        width=BUTTON_WIDTH,
        bg="#1e88e5",
        fg="white",
        activebackground="#1565c0",
        activeforeground="white",
        relief="flat",
        padx=16,
        pady=6,
        command=command,
    )
    info_btn = tk.Button(
        box,
        text="!",
        font=("Helvetica", 11, "bold"),
        bg="#c62828",
        fg="white",
        activebackground="#b71c1c",
        activeforeground="white",
        relief="flat",
        width=2,
        command=lambda: show_balloon(parent, hint_text, info_btn),
    )

    name.grid(row=row, column=1, padx=(20, 12), pady=12, sticky="e")
    btn.grid(row=row, column=2, padx=(12, 8), pady=12, sticky="w")
    info_btn.grid(row=row, column=3, padx=(0, 20), pady=12, sticky="w")


# -----------------------------------------------------------------------------
# Main UI
# -----------------------------------------------------------------------------


def build_ui():
    root = tk.Tk()
    root.title(WINDOW_TITLE)
    root.geometry(WINDOW_SIZE)
    root.configure(bg=BG_COLOR)

    # Fonts
    title_font = font.Font(family="Helvetica", size=32, weight="bold", underline=True)
    ui_font = font.Font(family="Helvetica", size=14)

    # Title
    title = tk.Label(root, text="Análise de Dados", font=title_font, bg=BG_COLOR, fg="#111")
    title.pack(pady=(30, 10))

    # Content box
    box = tk.Frame(root, bg=BG_COLOR, bd=1, relief="solid")
    box.pack(padx=40, pady=20, fill="x")

    box.grid_columnconfigure(0, weight=1)
    box.grid_columnconfigure(1, weight=0)
    box.grid_columnconfigure(2, weight=0)
    box.grid_columnconfigure(3, weight=0)
    box.grid_columnconfigure(4, weight=1)

    # Button rows
    rows = [
        ("Gerar Análise", "Iniciar", lambda: print("Gerar Análise"),
         'Caso tenha inserido dados novos "Upload de arquivos", use o botão "Atualizar" para o relatório incluir os novos dados. \n \nToque na mensagem para fechar!'),
        ("Atualizar Dados", "Atualizar", lambda: print("Atualizar Dados"),
         "Atualiza os dados inseridos em upload, use sempre que tiver inserido novos dados antes de gerar Análise. \n \nToque na mensagem para fechar!"),
        ("Upload de Arquivos", "Selecionar arquivo", lambda: print("Upload de Arquivos"),
         "Selecione os arquivos que serão analisados, você deve usar o botão atualizar para que os novos dados sejam carregados nas novas gerações de análise. \n \nToque na mensagem para fechar!"),
    ]

    for i, (name_text, btn_text, cmd, hint) in enumerate(rows):
        make_row(root, box, i, name_text, btn_text, cmd, hint, ui_font)

    root.mainloop()


if __name__ == "__main__":
    build_ui()


