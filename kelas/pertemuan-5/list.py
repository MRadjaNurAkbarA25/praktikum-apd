# Membaca Elemen List
praktikum = ['APD', 'OAK', 'Jarkom', ['RPL', 'Basis data', 'Strukdat']]
print(praktikum) #Membaca List termasuk Kurungnya

for i in praktikum: #Membaca List tanpa Memasukkan Kurung Siku
    print(i)
print(praktikum[3][1]) #Membaca Elemen dalam List

#Menambah Elemen List
praktikum.append('Web') #Menambah Elemen di Indeks paling belakang 
praktikum.insert(2, 'Strukdat') #Menambah Elemen ke indeks tertentu
print(praktikum)

tambah = input('Tambah :') #Menambah elemen yang diinput ke belakang
praktikum.append(tambah)
print(praktikum)

#Menghapus Elemen list
del praktikum[0] #Menghapus Elemen dengan Indeks
praktikum.remove('OAK') #Menghapus Elemen dengan Isi
buang = praktikum.pop() #Menampung Suatu Elemen dalam Satu Variabel Sendiri
print(praktikum)
print(buang)

#Membaca List dengan Start, Stop, Step (Slicing)
baca = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(baca[1 : 9 : 2]) #Mulai dari 2, stop di 8, lompat 2 angka
#Output > 2, 4, 6,8

mahasiswa = [["Daffa", "Dante", "Santoso"], ["Pernanda", "Triya", "Ahnaf"]] 
for i in mahasiswa:
    for j in i:
        print(j)
#Membaca Nested List  dengan perulangan

#Menambah dua list
nama = ['Radja', 'Yoga', 'Fina', 'Denny']
angka = [1, 2, 3, 4]
kombinasi = nama + angka
print(kombinasi)

#Tuple
anggota = ()