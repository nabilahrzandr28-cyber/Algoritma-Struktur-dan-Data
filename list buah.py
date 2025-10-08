 # list kosong
list_kosong = []

# list yang berisi kumpulan string
list_buah = ['Pisang', 'Nanas','Melon', 'Durian']

# list yang berisi kumpulan integer 
list_nilai = [80, 70, 90, 60]

# list campuran 
list_jawaban = [150, 33.33, 'Presiden Sukarno', False]
print('list_kosong:', list_kosong)
print('list_buah:', list_buah)
print('list_nilai:', list_nilai)
print('list_jawaban:', list_jawaban)
print(list_buah[0:1])
print(list_buah[0:2])
print(list_buah[1:3])
# ubah data pertama
list_buah[0] = 'Jeruk'

print(list_buah)

#ubah data terakhir
list_buah[-1] = 'Mangga'

print(list_buah)

#ubah data dalam range
list_buah[1:3] = ['Naga,''Pepaya']

print(list_buah)
#tambah data di belakang list
list_buah.append('sirsak')
print(list_buah)
# tambah data di awal list
list_buah.insert(2, 'Manggis')
print(list_buah)
list_buah.insert(0, 'Jambu')
print(list_buah)