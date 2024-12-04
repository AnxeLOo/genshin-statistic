import tkinter as tk

def display_message():
    root = tk.Tk()
    root.title("MENSAGEM DE ALERTA")
    label = tk.Label(root, text="Você é broxa!")
    label.pack(padx=20, pady=20)
    root.mainloop()

display_message()