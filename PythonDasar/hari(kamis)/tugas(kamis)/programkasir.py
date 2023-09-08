import tkinter as tk

def calculate_total():
    # Mengambil harga dan jumlah dari inputan pengguna
    harga = int(harga_entry.get())
    jumlah = int(jumlah_entry.get())

    # Menghitung total harga
    total = harga * jumlah

    # Menampilkan hasil pada label total_label
    total_label.config(text="Total : Rp " + str(total))

# Membuat window utama
window = tk.Tk()
window.title("Kasir Sederhana")

# Membuat label untuk input harga
harga_label = tk.Label(window, text="Harga:")
harga_label.pack()

# Membuat entry untuk input harga
harga_entry = tk.Entry(window)
harga_entry.pack()

# Membuat label untuk input jumlah
jumlah_label = tk.Label(window, text="Kuantitas:")
jumlah_label.pack()

# Membuat entry untuk input jumlah
jumlah_entry = tk.Entry(window)
jumlah_entry.pack()

# Membuat tombol untuk menghitung total harga
hitung_button = tk.Button(window, text="Hitung", command=calculate_total)
hitung_button.pack()

# Membuat label untuk menampilkan total harga
total_label = tk.Label(window, text="Total : Rp ")
total_label.pack()

# Menjalankan program
window.mainloop()
