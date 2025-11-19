# Program Total Belanja

# 1. Input jumlah item
jumlah = int(input("Masukkan jumlah item belanja: "))

# 2. Input harga setiap item
harga_list = []
for i in range(jumlah):
    harga = int(input(f"Masukkan harga item ke-{i+1}: "))
    harga_list.append(harga)

# 3. Hitung total
total = sum(harga_list)

# 4. Diskon jika total >= 300.000
if total >= 300000:
    total_akhir = total * 0.9   # diskon 10%
else:
    total_akhir = total

# 5. Tampilkan hasil
print("\nTotal belanja sebelum diskon:", total)
print("Total yang harus dibayar:", int(total_akhir))
