# Program Kategori Nilai Mahasiswa

# 1. Input list nilai
nilai_input = input("Masukkan nilai mahasiswa (pisahkan dengan koma): ")

# 2. Ubah menjadi list integer
nilai_list = [int(n.strip()) for n in nilai_input.split(",")]

# 3. Menampilkan kategori nilai
print("\nKategori Nilai:")
for nilai in nilai_list:
    if nilai >= 85:
        kategori = "A"
    elif nilai >= 70:
        kategori = "B"
    elif nilai >= 55:
        kategori = "C"
    else:
        kategori = "D"
    
    print(f"Nilai {nilai} = {kategori}")
