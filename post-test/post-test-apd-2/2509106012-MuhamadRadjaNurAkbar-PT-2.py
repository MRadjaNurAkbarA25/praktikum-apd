#Permintaan Input kepada User dan Mendklarasikan Variabelnya
nama_pasien = input('Masukkan nama pasien: ')
tinggi_badan = float(input('Masukkan tinggi badan anda dalam cm: '))
berat_badan = float(input('Masukkan berat badan anda dalam kg: '))

#Deklarasi Variabel
berat_ideal = (tinggi_badan - 100)
is_kelebihan = berat_badan > berat_ideal
statusList = ['Kelebihan berat badan', 'Berat badan seimbang']
status = statusList[int(is_kelebihan)]

#Kode Output
print(f'''--- HASIL CEK BERAT BADAN---
    Nama pasien   : {nama_pasien}
    Tinggi badan  : {tinggi_badan}
    Berat badan   : {berat_badan}
    Berat ideal   : {berat_ideal}
    Status        : {status}''')
