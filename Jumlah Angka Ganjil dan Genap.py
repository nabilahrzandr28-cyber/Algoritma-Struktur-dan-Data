# Program Hitung Ganjil dan Genap

angka_list = []

# Input 5 angka
for i in range(5):
    angka = int(input(f"Masukkan angka ke-{i+1}: "))
    angka_list.append(angka)

# Hitung ganjil & genap
genap = 0
ganjil = 0

for a in angka_list:
    if a % 2 == 0:
        genap += 1
    else:
        ganjil += 1

print("\nJumlah Angka Genap :", genap)
print("Jumlah Angka Ganjil:", ganjil)