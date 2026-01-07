# Meminta input usia dari pengguna
usia = int(input("Masukkan usia Anda: "))

# Menentukan kategori usia
if usia >= 0 and usia <= 5:
    print("Kategori usia: Balita")
elif usia >= 6 and usia <= 12:
    print("Kategori usia: Anak-anak")
elif usia >= 13 and usia <= 17:
    print("Kategori usia: Remaja")
elif usia >= 18 and usia <= 59:
    print("Kategori usia: Dewasa")
elif usia >= 60:
    print("Kategori usia: Lansia")
else:
    print("Usia tidak valid")