import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# init
window = tk.Tk()
window.configure(bg="white")
window.geometry("300x200")
window.resizable(False,False)
window.title("Sapa")

# Variabel
nama_depan = tk.StringVar()
nama_belakang = tk.StringVar()

# fungsi
def tombol_click():
    pesan = f"Hello {nama_depan.get()} {nama_belakang.get()}, Have a nice day bro"
    showinfo(title="Hi", message=pesan)

# frame input
input_frame = ttk.Frame(window)
input_frame.pack(padx=10, pady=10, fill="x", expand=True)

# komponen
#1. Label nama depan
nama_depan_label = ttk.Label(input_frame, text="Nama Depan:")
nama_depan_label.pack(padx=10, fill="x", expand=True)
#2. Entry nama depan
nama_depan_entry = ttk.Entry(input_frame, textvariable=nama_depan)
nama_depan_entry.pack(padx=10, fill="x", expand=True)
#3. Label nama belakang
nama_belakang_label = ttk.Label(input_frame, text="Nama Belakang:")
nama_belakang_label.pack(padx=10, fill="x", expand=True)
#4. Entry nama belakang
nama_belakang_entry = ttk.Entry(input_frame, textvariable=nama_belakang)
nama_belakang_entry.pack(padx=10, fill="x", expand=True)
#5.Tombol
tombol = ttk.Button(input_frame, text="Sapa!", command=tombol_click)
tombol.pack(fil="x", expand=True, padx=10, pady=10)

window.mainloop()