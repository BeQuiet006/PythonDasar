data = int(input("pilih = 1.Hitung Persegi panjang \n\t2.Hitung Trapesium\n\t(1/2) = "))

if data == 1:
    p = float(input("Masukan Panjang = "))
    l = float(input("Masukan Luas = "))
    s = float(input("Masukan Lebar = "))
    k = float(input("Masukan Keliling = "))
    rumusLuas = int(p * l)
    rumusKeliling = int(2 * (p + 1))
    rumusLebar = int(l + p)
    print(f"\n\nPanjang Segitiga {p} \nLuas Segitiga = {l} \nLebar segitiga = {s} \nKeliling Segitiga = {k}")
    print(f"Hasil Luas Segitiga = {rumusLuas}")
    print(f"Hasil Keliling Segitiga = {rumusKeliling}")
    print(f"Hasil Lebar Segitiga = {rumusLebar}")
elif data == 2:
    panjang2 = float(input("Masukan Panjang Sisi Sejajar Yang Pendek = "))
    panjang1 = float(input("Masukan Panjang Sisi Sejajar Yang Panjang = "))
    tinggi = float(input("Masukan Tinggi = "))
    rumusTrapesium = 1/2 * (panjang1 + panjang2) * tinggi
    print(f"Hasil Menghitung Trapesium = {rumusTrapesium}")
else:
    print("Something Wrong")
