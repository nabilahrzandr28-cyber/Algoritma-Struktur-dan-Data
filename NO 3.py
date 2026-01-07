def hitung_gaji(tarif_per_jam, jam_kerja_per_hari, hari_kerja):
    total_gaji = 0

    for i in range(hari_kerja):
        if jam_kerja_per_hari <= 6:
            total_gaji += jam_kerja_per_hari * tarif_per_jam
        else: 
            lembur = jam_kerja_per_hari
            total_gaji += (6 * tarif_per_jam) + (lembur * tarif_per_jam * 1,5)

    return total_gaji

tarif = int(input("masukkan tarif gaji per jam: "))
jam = int(input("masukkan jam kerja per hari: "))
hari = int(input("masukkan jumlah hari kerja: "))

total = hitung_gaji(50000, 6, 26)
print(f"total gaji bulanan: Rp {total}")