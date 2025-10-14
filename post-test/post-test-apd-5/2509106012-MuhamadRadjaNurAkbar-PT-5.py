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
        print('''===Menu===
1. Login
2. Register
3. Keluar''')
        menu = input('Pilih menu:')
        
        if menu == '1': #Menu login
            while True:
                print('Login akun')
                while True:
                    usr = input('Username\t:')
                    if usr.strip() != '': #Mencegah isi input yang kosong dengan .strip()
                        break #Jika variabel tidak kosong (!=) maka loop while akan break 
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
                        role = u[2] #Setelah usr dan pw benar, role akan di set ke role yang ada di list
                        break
                if loginn: 
                    os.system ('cls || clear')
                    print('Login berhasil!')
                    time.sleep(1) #Jeda sebelum menuju menu admin/users
                    break
                else:
                    os.system ('cls || clear')
                    print('Username atau Password salah!')
            if loginn: #Untuk memberhentikan loop login dan lanjut ke loop admin/user
                break
            
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
                    print('Username sudah terpakai')
                else:
                    while True:
                        pw_baru = input('Password baru\t:')
                        if len(pw_baru) < 3: #Mencegah jumlah karakter password di bawah 3
                            print('Password minimal berjumlah 3 karakter!')
                        else: 
                            break
                    users.append([usr_baru, pw_baru, 'user'])
                    os.system ('cls || clear')
                    print('Register berhasil!')
                    break
                
        elif menu == '3': #Keluar
            os.system('cls || clear')
            konfirmasiKeluar = input('Yakin ingin keluar?(y/n):')
            if konfirmasiKeluar == 'y':
                os.system('cls || clear')
                print('Anda menekan tombol keluar! Terima kasih telah menggunakan program ini!')
                exit() #Keluar dari program
            elif konfirmasiKeluar == 'n':
                print('Kembali ke program')
            else:
                print('Pilihan tidak valid!')
            
        else: #Pilihan di luar opsi
            os.system ('cls || clear')
            print('Pilihan tidak valid!')
    
    while True:
        if role == 'admin': #Menu admin
            print(f'Halo, {usr}!')
            print('''===MENU ADMIN===
1. Lihat barang
2. Tambah barang
3. Ubah data barang
4. Hapus barang
5. Log-out
6. Keluar''')
            menu_admin = input('Pilih menu:')  
        
            if menu_admin == '1': #Lihat barang, READ
                os.system ('cls || clear')
                print('Daftar barang')
                tabel.clear_rows() #Membersihkan tabel yang berulang
                
                for item in inventaris:
                    tabel.add_row(item)
                print(tabel) #Daftar barang ditunjukkan dalam bentuk tabel
                banyak_barang = len(inventaris) #len untuk menghitung jumlah barang, jumlah nested list 
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
                    if jumlah_input.isdigit() and int(jumlah_input) > 0: #Mencegah jumlah barang diisi dengan huruf atau 0, dan kosong
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
                            
            elif menu_admin == '3':
                os.system('cls || clear')
                print('Ubah data barang')
                print('Daftar barang')
                tabel.clear_rows()
                
                for item in inventaris:
                    tabel.add_row(item)
                print(tabel)
                while True:
                    #Membaca apakah kode barang yang diinput ada di list inventaris
                    cari_kode = input('Masukkan kode barang yang ingin diubah: ')
                    if cari_kode.strip() != '':
                        break
                    else:
                        print('Tidak boleh kosong!')
                os.system('cls || clear')
                ditemukan = False
                
                for ubah_barang in inventaris: #variabel ubah_barang akan terus digunakan dalam UPDATE
                    if ubah_barang[1] == cari_kode: #Juga menggunakan read
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
4. Ubah kondisi''')
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
                                tamkur = input('Pilih (1/2): ') #tamkur = tambah kurang
                                if tamkur in ['1', '2']: #jika input tamkur adalah 1/2, maka lanjut
                                    break
                                else:
                                    print('Pilihan tidak valid!')
                            while True:
                                jumlah_tamkur = input('Masukkan jumlah: ')
                                if jumlah_tamkur.isdigit() and int(jumlah_tamkur) > 0: #Mencegah jumlah barang diisi dengan huruf atau 0, dan kosong
                                    proses_operasional = int(jumlah_tamkur) #Variabel yang nilainya sama dengan variabel lain 
                                    
                                    if tamkur == '1':
                                        ubah_barang[2] += proses_operasional #Menambah jumlah barang
                                        print('Jumlah barang berhasil ditambahkan!')
                                        break
                                    
                                    elif tamkur == '2':
                                        if ubah_barang[2] >= proses_operasional: #Mencegah jumlah barang yang ingin kurangi lebih besar dari jumlah saat ini
                                            ubah_barang[2] -= proses_operasional
                                            print('Jumlah barang berhasil dikurangi!')
                                            break
                                        else:
                                            print('Jumlah terlalu besar untuk dikurangi')
                                else:
                                    print('Harus berupa angka lebih dari 0!')
                                
                        elif pilihan_ubah == '3': #Update kategori barang
                            os.system('cls || clear')
                            while True:
                                ubah_barang[3] = input('Ubah kategori barang: ')
                                if ubah_barang[3].strip() != '':
                                    break
                                else:
                                    print('Kategori barang tidak boleh kosong!')
                            print('Kategori berhasil diubah!')
                            
                        elif pilihan_ubah == '4': #Update kondisi barang
                            os.system('cls || clear')
                            while True:
                                ubah_barang[4] = input('Ubah kondisi barang: ')
                                if ubah_barang[4].strip() != '':
                                    break
                                else:
                                    print('Kondisi barang tidak boleh kosong!')
                            print('Kondisi barang berhasil diubah')
                            
                        else:
                            os.system('cls || clear')
                            print('Pilihan tidak valid')
                        break
                if not ditemukan:
                    #Kode barang yang tidak sesuai bernilai false, sehingga kode ini jalan
                    os.system('cls || clear')
                    print('Kode barang tidak ditemukan')
        
            elif menu_admin == '4': #DELETE, menghapus barang
                os.system('cls || clear')
                print('Daftar barang')
                
                tabel.clear_rows()
                
                for item in inventaris:
                    tabel.add_row(item)
                print(tabel)
                print('Hapus barang')
                
                while True:
                    hapus = input('Masukkan kode barang yang ingin dihapus: ')
                    if hapus.strip() != '':
                        break
                    else:
                        print('Tidak boleh kosong!')
                ketemu = False
                
                for hapus_barang in inventaris: #Membaca apakah kode barang yang diinput ada di list inventaris
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
                
        else: #Menu user
            print(f'Halo, {usr}!')
            print('''===MENU USER===
1. Lihat barang
2. Log-out
3. Keluar''')
            menu_user = input('Pilih menu: ')
            if menu_user == '1':
                os.system('cls || clear')
                print('Daftar barang')
                
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
#Selesai 