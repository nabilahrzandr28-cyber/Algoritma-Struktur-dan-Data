# Program Menu Nama

nama_list = []

while True:
    print("\n=== MENU ===")
    print("1. Tambah Nama")
    print("2. Hapus Nama")
    print("3. Tampilkan Semua Nama")
    print("4. Keluar")

    pilihan = input("Pilih menu (1-4): ")

    if pilihan == "1":
        nama = input("Masukkan nama yang ingin ditambahkan: ")
        nama_list.append(nama)
        print("Nama berhasil ditambahkan.")

    elif pilihan == "2":
        nama = input("Masukkan nama yang ingin dihapus: ")
        if nama in nama_list:
            nama_list.remove(nama)
            print("Nama berhasil dihapus.")
        else:
            print("Nama tidak ditemukan.")

    elif pilihan == "3":
        print("\nDaftar Nama:")
        if len(nama_list) == 0:
            print("Belum ada data.")
        else:
            for n in nama_list:
                print("-", n)

    elif pilihan == "4":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid, coba lagi.")
