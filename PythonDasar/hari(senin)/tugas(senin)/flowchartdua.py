namaKaryawan = str(input("Masukan Nama Anda = "))
gajiPokok = float(input("Masukan Gaji Anda = "))

tunjangan = 20/100 * gajiPokok
pajak = 15/100 * gajiPokok * tunjangan
gajiBersih = gajiPokok + tunjangan - pajak

print(f"\nNama Anda = {namaKaryawan}")
print(f"Gaji Pokok Anda = {gajiPokok}")
print(f"Tunjungan Anda = {tunjangan}")
print(f"Pajak Anda = {pajak}")
print(f"Gaji Bersih Anda = {gajiBersih}")