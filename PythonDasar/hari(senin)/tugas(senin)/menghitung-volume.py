list = int(input("Pilih Salah Satu = 1.Menghitung Volume Tabung\n\t\t   2.Menghitung Balok\n\t\t(1/2) = "))

if list == 1:
    a = float(input("Masukan Luas Alas Tabung = "))
    b = float(input("Masukan Tinggi Tabung = "))
    RumusVolumeTabung = a * b
    print(f"Hasil Volume Tabung = {RumusVolumeTabung}")
elif list == 2:
    c = float(input("Masukan Volume balok = "))
    d = float(input("Masukan Panjang Balok = "))
    e = float(input("Masukan Lebar Balok = "))
    f = float(input("Masukan Tinggi Balok = "))
    rumusVolumeBalok = d * e * f
    print(f"Hasil Menghitung Volume Balok = {rumusVolumeBalok}")
else:
    ("Something Wrong")