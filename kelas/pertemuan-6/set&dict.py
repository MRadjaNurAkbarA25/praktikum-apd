# #Membuat set
# buah = {'apel', 'anggur', 'jeruk', 'mangga'}
# print(buah)

# #Memanggil elemen set satu-satu
# angka_ganjil = {1, 3, 5, 7, 9}
# for angka in angka_ganjil:
#     print (angka)
    
# #Mengubah list menjadi set
# friend = ['asep', 'ucup', 'didi']
# tes = set(friend)
# print(set)

# #Dictionary
# Daftar_buku = {
# "Buku1" : "Bumi Manusia",
# "Buku2" : "Laut Bercerita"
# }
# print(Daftar_buku["Buku1"])
# print(Daftar_buku)

# Biodata = {
# "Nama" : "Ananda Daffa Harahap",
# "NIM" : 2409106050,
# "KRS" : ["Pemrograman Web", "Struktur Data", "Basis Data"],
# "Mahasiswa_Aktif" : True,
# "Social Media" : {
#     "Instagram" : "daffahrhap"
#     }
# }

# print(Biodata)
# for i in Biodata:
#     print(i, ':', Biodata[i])
# for i, j in Biodata.items():
#     print(f'Ini adalah key {i} dan ini adalah value {j}')

# print(f'nama saya adalah {Biodata['Nama']}')
# print(f'Instagram : {Biodata['Social Media']['Instagram']}')
# print(f'nama saya adalah {Biodata.get('Nama')}')
# print(Biodata.get('Nama'))

# Film = {
# "Avenger Endgame" : "Action",
# "Sherlock Holmes" : "Mystery",
# "The Conjuring" : "Horror"
# }

#Sebelum Ditambah
# print(Film)
# Film["Zombieland"] = "Comedy"
# Film.update({"Hours" : "Thriller"})
# #Setelah Ditambah
# print(Film)
# #Sebelum Ditambah
# {'Avenger Endgame': 'Action', 'Sherlock Holmes': 'Mystery',
# 'The Conjuring': 'Horror'}
# #Setelah Ditambah
# {'Avenger Endgame': 'Action', 'Sherlock Holmes': 'Mystery',
# 'The Conjuring': 'Horror', 'Zombieland': 'Comedy', 'Hours':
# 'Thriller'}

# hapus = Film.pop('The Conjuring')
# print(hapus)

# Musik = {
#     "The Chainsmoker": ["All we Know", "The Paris"],
#     "Alan Walker": ["Alone", "Lily"],
#     "Neffex": ["Best of Me",['tes','halo'], "Memories"],
#     'Paramore' : ["Misery Business", "Ain't It Fun", 
#                 ['All We Know Is Falling',['Here We Go Again', 'My Heart']],'This Is Why' ]
# }

# print(Musik['Paramore'][2][1][1])

# angka = {}
# print(type(a))

Nilai = {
"Matematika" : 80,
"B. Indonesia" : 90,
"B. Inggris" : 81
}