def hitung(a, b, op):
    if op == "1":
        return a + b
    elif op == "2":
        return a - b
    elif op == "3":
        return a * b
    elif op == "4":
        return "Error: Tidak bisa membagi dengan nol" if b == 0 else a / b
    else:
        return "Pilihan tidak valid"

print("=== Kalkulator Sederhana ===")
print("1. Penjumlahan\n2. Pengurangan\n3. Perkalian\n4. Pembagian")

op = input("Pilih operasi (1/2/3/4): ")
a = float(input("Masukkan angka pertama: "))
b = float(input("Masukkan angka kedua: "))

print("Hasil:", hitung(a, b, op))
