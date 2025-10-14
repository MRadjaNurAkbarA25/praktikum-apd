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

#Role default sebelum register
#Status variabel untuk menentukan logika berikutnya

while True: #Loop utama program
    role = None
    loginn = False
    while True:
        print('''===MAIN MENU===
1. Login
2. Register
3. Keluar''') #Main menu
        menu = input('Silahkan pilih opsi:')
        
        if menu == '1': #Menu login
            while True:
                print('Login akun')
                while True:
                    usr = input('Username\t:')
                    if usr.strip() != '':
                        break
                    else:
                        print('Username tidak boleh kosong!')
                while True:        
                    pw = input('Password\t:')
                    if pw.strip() != '':
                        break
                    else:
                        print('Password tidak boleh kosong!')
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
            
        elif menu == '2': #Menu register
            os.system ('cls || clear')
            print('Registrasi')
            while True:
                cek_ada_usr = False #variabel untuk mencegah username yang sudah digunakan
                while True:
                    usr_baru = input('Username baru\t:')
                    if usr_baru.strip() != '':
                        break
                    else:
                        print('Username tidak boleh kosong!')
                for u in users: #Jika username yang baru sudah digunakan, status jadi True
                    if usr_baru == u[0]:
                        cek_ada_usr = True
                        break
                if cek_ada_usr:
                    print('Username sudah terpakai!')
                else:
                    while True:
                        pw_baru = input('Password\t:')
                        if pw_baru.strip() == '':
                            print('Password tidak boleh kosong!')
                        elif len(pw_baru) < 3:
                            print('Password minimal berjumlah 3 karakter!')
                        else: 
                            break
                    users.append([usr_baru, pw_baru, 'user'])
                    os.system ('cls || clear')
                    print('Register berhasil!')
                    break
                
        elif menu == '3': #Keluar
            os.system ('cls || clear')
            print('Anda menekan tombol keluar! Terima kasih telah menggunakan program ini!')
            exit()
            
        else: #Pilihan di luar opsi
            os.system ('cls || clear')
            print('Pilihan tidak valid!')
    
    while True:
        if role == 'admin': #Menu admin
            print(f'Halo, {usr}!')
            print('''Pilih menu
1. Lihat barang
2. Tambah barang
3. Ubah data barang
4. Hapus barang
5. Log-out
6. Keluar''')
            menu_admin = input('Pilih menu:')  
        
            if menu_admin == '1': #Lihat barang, READ
                os.system ('cls || clear')
                print('Barang di kantor saat ini')
                
                tabel.clear_rows()
                
                for item in inventaris:
                    tabel.add_row(item)
                print(tabel)
                banyak_barang = len(inventaris)
                print(f'Jumlah barang: {banyak_barang}')
            
            elif menu_admin == '2':
                os.system ('cls || clear')
                print('Tambah barang')
                
                while True: #Nama barang baru
                    barang_baru = input('Nama barang\t:') 
                    if barang_baru.strip() != '':
                        break
                    else:
                        print('Nama barang tidak boleh kosong!')
                        
                while True: #Kode barang baru
                    cek_kode_barang = False 
                    print('Contoh kode barang: BRG001, BRG002')
                    while True:
                        kode_barang = input('Kode barang\t:') 
                        if kode_barang.strip() != '':
                            break
                        else:
                            print('Kode barang tidak boleh kosong')
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
                        print('Jumlah harus tidak boleh kosong dan harus berupa angka lebih dari 0!')
                while True:        
                    kategori_barang = input('Kategori barang\t:') #Kategori barang baru
                    if kategori_barang.strip() != '':
                        break
                    else:
                        print('Kategori barang tidak boleh kosong')
                while True:
                    kondisi_barang = input('Kondisi barang\t:') #Kondisi barang baru
                    if kondisi_barang.strip () != '':
                        break
                    else:
                        print('Kondisi barang tidak boleh kosong!')
                #Menambah barang baru ke belakang list inventaris sebagai nested list
                inventaris.append([barang_baru, kode_barang, jumlah_barang,  kategori_barang, kondisi_barang])
                os.system('cls || clear')
                print('Barang berhasil ditambahkan!')
                time.sleep[1]
                continue
            
            elif menu_admin == '3':
                os.system('cls || clear')
                print('Ubah data barang')
                print('Barang di kantor saat ini')
                
                tabel.clear_rows()
                
                for item in inventaris:
                    tabel.add_row(item)
                print(tabel)
                while True:
                    cari_kode = input('Masukkan kode barang yang ingin diubah: ')
                    if cari_kode.strip() != '':
                        break
                    else:
                        print('Tidak boleh kosong!')
                os.system('cls || clear')
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
1. Ubah nama barang
2. Ubah jumlah barang
3. Ubah kategori
4. Ubah kondisi
5. Batalkan''')
                        pilihan_ubah = input('Pilih apa yang ingin diubah: ')
                        
                        if pilihan_ubah == '1':
                            while True:
                                ubah_barang[0] = input('Ubah nama barang: ')
                                if ubah_barang[0].strip() != '':
                                    break
                                else:
                                    print('Nama barang tidak boleh kosong!')
                            os.system('cls || clear')
                            print('Nama barang berhasil diubah!')
                            
                        elif pilihan_ubah == '2':
                            os.system('cls || clear')
                            print('Ubah jumlah barang: ')
                            print(f'Jumlah barang saat ini: {ubah_barang[2]}')
                            print('''Pilih:
1. Tambah jumlah barang
2. Kurangi jumlah barang''')
                            while True:
                                tamkur = input('Pilih (1/2): ')
                                if tamkur in ['1', '2']:
                                    break
                                else:
                                    print('Pilihan tidak valid! Pilih 1 atau 2')
                            while True:
                                jumlah_tamkur = input('Masukkan jumlah: ')
                                if jumlah_tamkur.isdigit() and int(jumlah_tamkur) > 0:
                                    proses_operasional = int(jumlah_tamkur)
                                    break
                                else:
                                    print('Harus berupa angka lebih dari 0!')
                                    
                            if tamkur == '1':
                                ubah_barang[2] += proses_operasional
                                print('Jumlah barang berhasil ditambahkan!')
                            elif tamkur == '2':
                                if ubah_barang[2] >= proses_operasional:
                                    ubah_barang[2] -= proses_operasional
                                    print('Jumlah barang berhasil dikurangi!')
                                else:
                                    print('Jumlah terlalu besar untuk dikurangi')
                                
                        elif pilihan_ubah == '3':
                            os.system('cls || clear')
                            while True:
                                ubah_barang[3] = input('Ubah kategori barang: ')
                                if ubah_barang[3].strip() != '':
                                    break
                                else:
                                    print('Kategori barang tidak boleh kosong!')
                            print('Kategori berhasil diubah!')
                            
                        elif pilihan_ubah == '4':
                            os.system('cls || clear')
                            while True:
                                ubah_barang[4] = input('Ubah kondisi barang: ')
                                if ubah_barang[4].strip() != '':
                                    break
                                else:
                                    print('Kondisi barang tidak boleh kosong!')
                            print('Kondisi barang berhasil diubah')
                            
                        elif pilihan_ubah == '5':
                            os.system('cls || clear')
                            print('Perubahan dibatalkan!')
                        else:
                            os.system('cls || clear')
                            print('Pilihan tidak valid')
                        break
                if not ditemukan:
                    os.system('cls || clear')
                    print('Kode barang tidak ditemukan')
        
            elif menu_admin == '4':
                os.system('cls || clear')
                print('Hapus barang')
                
                while True:
                    hapus = input('Masukkan kode barang yang ingin dihapus: ')
                    if hapus.strip() != '':
                        break
                    else:
                        print('Tidak boleh kosong!')
                ketemu = False
                
                for hapus_barang in inventaris:
                    if hapus_barang[1] == hapus:
                        ketemu = True
                        print(f'''
Data ditemukan:
Nama\t\t: {hapus_barang[0]}
Kode\t\t: {hapus_barang[1]}
Jumlah\t\t: {hapus_barang[2]}
Kategori\t: {hapus_barang[3]}
Kondisi\t\t: {hapus_barang[4]}''')
                        konfirmasi = input('Konfirmasi hapus barang?(y/n):')
                        if konfirmasi == 'y':
                            os.system('cls || clear')
                            inventaris.remove(hapus_barang)
                            print('Barang berhasil dihapus')
                        elif konfirmasi == 'n':
                            os.system('cls || clear')
                            print('Penghapusan dibatalkan')
                        else:
                            os.system('cls || clear')
                            print('Tidak dalam pilihan!')
                        break
                if not ketemu:
                    print('Kode barang tidak ditemukan!')
                    
            elif menu_admin == '5':
                os.system('cls || clear')
                konfirmasi1 = input('Yakin ingin log-out?(y/n): ')
                if konfirmasi1 == 'y':
                    os.system('cls || clear')
                    print('Kamu menekan tombol log-out!')
                    break
                elif konfirmasi1 == 'n':
                    print('Log-out dibatalkan')
                else:
                    print('Pilihan tidak valid!')

            elif menu_admin == '6':
                os.system('cls || clear')
                konfirmasi2 = input('Yakin ingin keluar?(y/n):')
                if konfirmasi2 == 'y':
                    os.system('cls || clear')
                    print('Anda menekan tombol keluar! Terima kasih telah menggunakan program ini!')
                    exit() #Keluar dari program
                elif konfirmasi2 == 'n':
                    print('Kembali ke program')
                else:
                    print('Pilihan tidak valid!')
                
            else:
                os.system('cls || clear')
                print('Pilihan tidak valid!')
                
        elif role == 'user':
            print(f'Halo, {usr}!')
            print('''Pilih menu
1. Lihat barang
2. Log-out
3. Keluar''')
            menu_user = input('Pilih menu: ')
            if menu_user == '1':
                os.system('cls || clear')
                print('Barang di kantor saat ini')
                
                tabel.clear_rows()
                
                for item in inventaris:
                    tabel.add_row(item)
                print(tabel)
                banyak_barang = len(inventaris)
                print(f'Jumlah barang: {banyak_barang}')
                
            elif menu_user == '2':
                os.system('cls || clear')
                konfirmasi3 = input('Yakin ingin log-out?(y/n): ')
                if konfirmasi3 == 'y':
                    os.system('cls || clear')
                    print('Kamu menekan tombol log-out!')
                    break
                elif konfirmasi3 == 'n':
                    print('Log-out dibatalkan')
                else:
                    print('Pilihan tidak valid!')
            
            elif menu_user == '3':
                os.system('cls || clear')
                konfirmasi4 = input('Yakin ingin keluar?(y/n):')
                if konfirmasi4 == 'y':
                    os.system('cls || clear')
                    print('Anda menekan tombol keluar! Terima kasih telah menggunakan program ini!')
                    exit() #Keluar dari program
                elif konfirmasi4 == 'n':
                    print('Kembali ke program')
                else:
                    print('Pilihan tidak valid!')
                
            else: 
                os.system('cls || clear')
                print('Pilihan tidak valid!')
