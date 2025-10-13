import os
import time
from prettytable import PrettyTable
#Nested list ['Nama barang', 'Kode barang', Jumlah, 'Kategori', 'Kondisi']
inventaris = [
    ['Monitor', 'BRG001', 7, 'Elektronik', 'Baik'], 
    ['Meja kayu', 'BRG002', 10, 'Perabot', 'Baik'],
    ['Buku catatan', 'BRG003', 30,  'Alat tulis', 'Baik'], 
    ['Kursi plastik','BRG004', 20, 'Perabot', 'Baik'],
    ['Printer', 'BRG005', 5, 'Elektronik', 'Baik'],
    ['Pulpen', 'BRG006', 60, 'Alat tulis', 'Baik'],
    ['PC', 'BRG007', 7, 'Elektronik', 'Baik']
] #<---- List barang awal
users = [['radja', '012', 'admin']] #List untuk akun

#Susunan untuk membuat tabel dengan PrettyTable
tabel = PrettyTable ()
#Setiap elemen memiliki kolom sendiri
tabel.field_names = ['Nama barang', 'Kode', 'Jumlah', 'Kategori', 'Kondisi']

role = None #Role default sebelum register
loginn = False #Status variabel untuk menentukan logika berikutnya

while True: #Logika menu terus berjalan hingga berhasil login/register
    print('---Pengelolaan Inventaris Barang Kantor---') #Logika menu
    print('''===Menu===
1. Login
2. Register
3. Keluar''')
    menu = input('Silahkan pilih opsi:')
    if menu == '1': #Menu login
        while True:
            print('Login akun')
            usr = input('Username\t:')
            pw = input('Password\t:')
            for u in users: #Menggunakan for untuk membaca nested list
                #for agar bisa langsung membaca semua elemen termasuk yang ada di dalam nested list
                if usr == u[0] and str(pw) == u[1]: 
                    loginn = True #Status loginn menjadi True jika usr & pw benar
                    role = u[2]
                    break
            if loginn: 
                os.system ('cls || clear')
                print('Login berhasil!')
                time.sleep(1) #Jeda sebelum menuju menu admin dan users
                break
            else:
                os.system ('cls || clear')
                print('Username atau Password salah!')
        if loginn:
            break
    elif menu == '2': #Menu register
        os.system ('cls || clear')
        print('Registrasi')
        while True:
            cek_ada_usr = False #variabel untuk mencegah username yang sudah digunakan
            usr_baru = input('Username baru\t:')
            for u in users: #Jika username yang baru sudah digunakan, status jadi True
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
    elif menu == '3': #Keluar
        os.system ('cls || clear')
        print('Anda menekan tombol keluar! Terima kasih telah menggunakan program ini!')
        break
    else: #Pilihan di luar opsi
        os.system ('cls || clear')
        print('Pilihan tidak dalam menu!')
        
if loginn: #Menu admin dan users
    while True:
        if role == 'admin': #Menu admin
            print('Halo, radja!')
            print('''Pilih menu
1. Lihat barang
2. Tambah barang
3. Ubah data barang
4. Hapus barang
5. Kembali
6. Keluar''')
        menu_admin = input('Pilih menu:')  
        
        if menu_admin == '1': #Lihat barang, READ
            os.system ('cls || clear')
            print('Barang di kantor saat ini')
            for item in inventaris:
                tabel.add_row(item)
            print(tabel)
            banyak_barang = len(inventaris)
            print(f'Jumlah barang: {banyak_barang}')
            
        elif menu_admin == '2':
            os.system ('cls || clear')
            print('Tambah barang')
            barang_baru = input('Nama barang\t:') #Nama barang baru
            while True:
                cek_kode_barang = False 
                print('Contoh kode barang: BRG001, BRG002')
                kode_barang = input('Kode barang\t:') #Kode barang baru
                for j in inventaris: #Mencegah kode barang baru sama dengan di inventaris
                    if kode_barang == j[1]:
                        cek_kode_barang = True
                        break
                if cek_kode_barang:
                    print('Kode barang sudah digunakan! Gunakan kode lain')
                else:
                    break
                
            while True:
                jumlah_input = input('Jumlah barang\t:') #Jumlah barang baru
                if jumlah_input.isdigit() and int(jumlah_input) > 0: #Mencegah jumlah barang diisi dengan huruf atau 0
                    jumlah_barang = int(jumlah_input)
                    break
                else:
                    print('Jumlah harus berupa angka lebih dari 0!')
                    
            kategori_barang = input('Kategori barang\t:') #Kategori barang baru
            kondisi_barang = input('Kondisi barang\t:') #Kondisi barang baru
            #Menambah barang baru ke belakang list inventaris sebagai nested list
            inventaris.append([barang_baru, kode_barang, jumlah_barang,  kategori_barang, kondisi_barang])
            os.system('cls || clear')
            print('Barang berhasil ditambahkan!')
            continue
            
        elif menu_admin == '3':
            print('Ubah data barang')
            cari_kode = input('Masukkan kode barang yang ingin diubah: ')
            ditemukan = False
            
            for ubah_barang in inventaris:
                if ubah_barang[1] == cari_kode:
                    ditemukan = True
                    print(f'''
Data ditemukan:
Nama\t\t: {ubah_barang[0]}
Kode\t\t: {ubah_barang[1]}
Jumlah\t\t: {ubah_barang[2]}
Kategori\t: {ubah_barang[3]}
Kondisi\t\t: {ubah_barang[4]}''')
                    
                    print('''Pilih data yang ingin diubah:
1. Ubah jumlah barang
2. Ubah kategori
3. Ubah kondisi
4. Ubah nama barang
5. Batalkan''')
                    pilihan_ubah = input('Pilih apa yang ingin diubah: ')

            
        else:
            print('dad')