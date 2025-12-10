listkota = [
    'Jakarta', 'Surabaya', 'Depok', 'Bekasi', 'Solo', 'Yogyakarta', 'Semarang', 'Makasar'
]

for i, kota in enumerate(listkota):
    print(i, kota) 
else:
    print('Tidak ada lagi item yang tersisa')

listkota = [
    'Jakarta', 'Surabaya', 'Depok', 'Bekasi', 'Solo', 'Yogyakarta', 'Semarang', 'Makasar'
]
kotaYangDicari = input('Ketik nama kota yang kamu cari: ')
for i, kota in enumerate(listkota):
    #kita ubah katanya ke Lowercase agar
    # menjadi case insensitive
    if kota.lower() == kotaYangDicari.lower():
        print('kota yang anda cari berada pada indeks', i)
        break
else: 
    print('Maaf, kota yang anda cari tidak ada') 
    