import os
import time
from prettytable import PrettyTable
#Nested list ['Nama barang', 'Kode barang', 'Lokasi, 'Kondisi']
inventaris = [
    ['Laptop', '0001', 'Ruang IT', 'Baik'], 
    ['Meja kayu', '0002', 'Ruang dosen', 'Baik'],
    ['Buku catatan', '0003', 'Gudang', 'Baik'], 
    ['Kursi plastik','0004', 'Aula', 'Baik'],
    ['Printer', '0005', 'Ruang IT', 'Baik'],
    ['Pulpen', '0006', 'Ruang Dosen', 'Baik']
]

tabel = PrettyTable()
tabel.field_names = ['Nama barang', 'Kode', 'Lokasi', 'Kondisi']
users = [['radja', '012', 'admin']] #List untuk user
role = None

while True: #Logika menu terus berjalan hingga berhasil login/register
    print('---Pengelolaan Inventaris Barang Kantor---') #Logika menu
    print('''===Menu===
1. Login
2. Register
3. Keluar''')
    menu = int(input('Silahkan pilih opsi:'))
    if menu == 1: #Menu login
        loginn = False #Menggunakan boolean untuk melanjutkan statusnya
        print('Login')
        usr = input('Username\t:')
        pw = input('Password\t:')
        for u in users: #Menggunakan for untuk membaca nested list
            #for agar bisa langsung membaca semua elemen termasuk yang di dalam nested list
            if usr == u[0] and str(pw) == u[1]: 
                loginn = True #Status loginn menjadi True jika usr & pw benar
                role = u[2]
                break
        if loginn: 
            os.system ('cls || clear')
            print('Login berhasil!')
            time.sleep(1)
        else:
            os.system ('cls || clear')
            print('Username atau Password salah')
    elif menu == 2: #Menu register
        while True:
            cek_ada_usr = False #variabel untuk mencegah username yang sama
            usr_baru = input('Username baru\t:')
            for u in users:
                if usr_baru == u[0]:
                    cek_ada_usr = True
                    break
            if cek_ada_usr:
                print('Username sudah digunakan, masukkan username lain')
            else:
                pw_baru = input('Password baru\t:')
                users.append([usr_baru, pw_baru, 'user'])
                for u in users:
                    role = u[2]
                os.system ('cls || clear')
                print('Register berhasil! Akun ditambahkan')
                break
    elif menu == 3: #Keluar
        os.system ('cls || clear')
        print('Anda menekan tombol keluar! Terima kasih telah menggunakan program ini!')
        break
    else: #Pilihan di luar opsi
        os.system ('cls || clear')
        print('Pilihan tidak dalam menu!')

    while True:
        if role == 'admin':
            print('''Pilih menu
1. Lihat barang
2. Tambah barang
3. Ubah data barang
4. Hapus barang
5. Keluar''')
            
        if menu_admin == 1:
            print('Barang di kantor saat ini')
            for item in inventaris:
                tabel.add_row(item)
            print(tabel)
            menu_admin = int(input('Pilih menu:'))
        elif menu_admin == 2:
                kode_barang_cek = False
                barang_baru = input('Nama barang\t:')
                print('Contoh kode barang: 0001, 0002')
                kode_barang = input('Kode barang\t:')
                for j in inventaris:
                    if kode_barang == j[1]:
                        kode_barang_cek = True
                        break
                if kode_barang_cek:
                    print('Kode barang sudah digunakan! Gunakan kode lain')
                else:
                    lokasi_barang = input('Lokasi barang\t:')
                    kondisi_barang = input('Kondisi barang\t:')
                    inventaris.append([barang_baru, kode_barang, lokasi_barang, kondisi_barang])
                    print('Barang berhasil ditambahkan!')
                    for i in inventaris:
                        print(f'''Barang\t: {i[0]}
Kode barang\t:{i[1]}
Lokasi\t: {i[2]}
Kondisi\t: {i[3]}
''')
        else:
            print('dad')
        break

