# nilai = 70

# if nilai > 75:
#     print('Nilai A')
# elif nilai > 65:
#     print('Nilai B')
# else:
#     print('Nilai C')

# suhu = 35

# if suhu >= 35:
#     print('Panas')
# if suhu > 30:
#     print('Sauna')
# elif suhu > 20:
#     print('Normal')
# else:
#     print('Dingin')

# umur = int(input("Masukkan umur Anda: "))
#  misalnya, umur = 16
#  Percabangan
# if umur < 13:
#     kategori = "Anak-anak"
# elif umur < 18:
#     kategori = "Remaja"
# elif umur < 60:
#     kategori = "Dewasa"
# else:
#     kategori = "Lansia"
# Menampilkan umur dan kategori
# print("Umur:", umur, "Kategori:", kategori)

# status = 'Lulus' if nilai >= 60 else 'Tidak lulus'
# print(status)

# tinggi_badan = float(input('Masukkan tinggi badan:'))
# if tinggi_badan >= 145:
#     print('Boleh masuk')
# else:
#     print('Tidak boleh masuk')

# tinggi = 130
# print(f'Tinggi: {tinggi} cm')
# Wahana = 'Boleh masuk' if tinggi >= 145 else 'Tidak boleh'
# print(Wahana)

print('---KALKULATOR BANGUN RUANG')
print('1.Kubus')
print('2.Balok')
print('3.Tabung')
print('4.Keluar')

pilih = input('Pilih bangun ruang yang diinginkan:')

if pilih =='1':
    print('---KALKULATOR KUBUS')
    sisi = float(input('Masukkan sisi kubus:'))
    volume = sisi**3
    print(f'Sisi Kubus: {sisi}')
    print(f'Volume Kubus: {volume} cm3')

elif pilih =='2':
    print('---KALKULATOR BALOK---')
    panjang = int(input('Masukkan panjang balok:'))
    lebar = int(input('Masukkan lebar balok:'))
    tinggi = int(input('Masukkan tinggi balok:'))
    volume = panjang *  lebar * tinggi
    print(f'Volume balok: {volume} cm3')

elif pilih =='3':
    print('---KALKULATOR TABUNG---')
    pi = 3.14
    jari_jari = float(input('Masukkan jari-jari: '))
    t = float(input('Masukkan tinggi:'))
    volume = pi * r**2 * t 
    print(f'Volume tabung : {volume} cm3')

elif pilih =='4':
    print('Terimakasih telah mencoba kalkulator bangun ruang')

else:
    print('Pilihan tidak dalam kategori')
