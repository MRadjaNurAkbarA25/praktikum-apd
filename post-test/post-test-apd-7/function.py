import os
import time
from prettytable import PrettyTable
from kamus import inventaris, users

def clear(): #Fungsi membersihkan terminal
    os.system('cls || clear')
    
def delay(): #Fungsi memberi jeda
    time.sleep(1)
    
def daftar(): #Fungsi menampilkan tabel barang
    tabel = PrettyTable ()
    tabel.field_names = ['Kode', 'Nama barang', 'Jumlah', 'Kategori', 'Kondisi']
    print('Daftar barang')
    tabel.clear_rows() 
    for item, data in inventaris.items():
        tabel.add_row([item, data['nama'], data['jumlah'], data['kategori'], data['kondisi'] ])
    return tabel

def tampil_menu_rekursif(menu_list, index = 0): #Fungsi rekursif untuk menampilkan menu
    #Base Case
    if index >= len(menu_list):
        return
    
    #Recursive Case
    print(f'{index + 1}. {menu_list[index]}')
    tampil_menu_rekursif(menu_list, index + 1)

def input_str(pesan): #Fungsi erorr handling untuk mencegah input kosong
    while True:
        try:
            fakta = input(pesan)
            if fakta.strip() == '':
                raise ValueError('Input tidak boleh kosong')
            return fakta
        except ValueError as e:
            print(e)  

def regist_pw(pesan): #Fungsi error handling untuk memasukkan password akun baru(registrasi)
    while True: #
        try:
            pw_baru = input(pesan)
            if len(pw_baru) < 3:
                raise ValueError('Password minimal 3 karakter!')
            return pw_baru
        except ValueError as e:
            print(e)

def jumlah(pesan): #Fungsi error handling untuk menginput jumlah dari opsi menambah barang baru
    while True:
        try:
            jumlah_input = input(pesan)
            if jumlah_input.strip() == '':
                raise ValueError('Input tidak boleh kosong!')
            jumlah_int = int(jumlah_input)
            if jumlah_int <= 0:
                raise ValueError('Jumlah harus lebih besar dari 0!')
            return jumlah_int
        except ValueError:
            if jumlah_input.strip() == '':
                print('Input tidak boleh kosong!')
            else:
                try:
                    if int(jumlah_input) <= 0:
                        print('Jumlah harus lebih besar dari 0!')
                except:
                    print('Input harus berupa angka!')

def login(): #Fungsi untuk login
    clear()
    print('Login akun')
    while True:
        #Variabel lokal
        usr = input_str('Masukkan Username\t:') 
        pw = input_str('Masukkan password\t:')
        
        for u in users:
            if usr == u and pw == users[u]['password']:
                role = users[u]['role']
                clear()
                print('Login berhasil!')
                delay()
                return usr, role
            else:
                clear()
                print('Username atau passsword salah!')

def register(): #Fungsi untuk registrasi
    clear()
    print('Register')
    while True:
        cek_ada_usr = False
        usr_baru = input_str('Masukkan username baru:')
        
        for u in users:
            if usr_baru == u:
                cek_ada_usr = True
                break
        if cek_ada_usr:
            print('Username sudah terpakai! Gunakan username lain')
        else:
            pw_baru = regist_pw('Masukkan password:')
            users.update({
                        usr_baru : {'password' : pw_baru, 
                                    'role' : 'user' 
                        }
                    })
            clear()
            print('Registrasi berhasil!')
            delay()
            return usr_baru, pw_baru

def keluar(): #Fungsi untuk keluar dari program
    clear()
    while True:
        konfirmasi = input('Yakin ingin keluar dari program?(y/n):')
        
        if konfirmasi.lower() == 'y':
            clear()
            print('Anda menekan tombol keluar! Terimakasih telah menggunakan program!')
            delay()
            exit()
        elif konfirmasi.lower() == 'n':
            print('Kembali ke program')
            delay()
            clear()
            return
        else:
            print('Input tidak valid!') 

#Contoh prosedur
def tambah_barang(): #Fungsi untuk menambah barang baru ke daftar barang
    while True:
        nama_barang = input_str('Nama barang:')
        
        while True:
            cek_kode = False
            kode_barang = input_str('Kode barang:')
                    
            for j in inventaris:
                if kode_barang == j:
                    cek_kode = True
                    break
            if cek_kode:
                print('Kode barang sudah terpakai! Gunakan kode lain!')
            else:
                break
                
        jumlah_barang = jumlah('Jumlah barang:')
        
        kategori_barang = input_str('Kategori barang\t:')
                
        kondisi_barang = input_str('Kondisi barang\t:')
        
        inventaris.update({
            kode_barang : {'nama' : nama_barang,
                        'jumlah' : jumlah_barang,
                        'kategori' : kategori_barang,
                        'kondisi' : kondisi_barang}
        })
        
        clear()
        print('Barang berhasil ditambahkan!')
        delay()
        return

def ubah_data(): #Fungsi mengubah data barang yang sudah ada
    ditemukan = False
    clear()
    print('Ubah data barang')
    print(daftar())
    
    cari_kode = input_str('Masukkan kode barang yang ingin diubah\t:')
    clear()
    
    for k in inventaris:
        if k == cari_kode:
            ditemukan = True
            ada = inventaris[k]
            print(f'''Data ditemukan:
Nama\t\t: {ada['nama']}
Kode\t\t: {k}
Jumlah\t\t: {ada['jumlah']}
Kategori\t: {ada['kategori']}
Kondisi\t\t: {ada['kondisi']}''')

            print('Pilih data yang ingin diubah:')
            menu_ubah_barang = ['Ubah nama barang', 'Ubah jumlah barang',
                                'Ubah kategori barang', 'Ubah kondisi barang']
            tampil_menu_rekursif(menu_ubah_barang)
            
            pilihan_ubah = input('Pilih apa yang ingin diubah: ')
            
            if pilihan_ubah == '1':
                nama_baru = input_str('Ubah nama barang:')
                inventaris[k]['nama'] = nama_baru   
                clear()
                print('Nama berhasil diubah!')
                delay()
                return
            
            if pilihan_ubah == '2':
                clear()
                
                print(f"Jumlah barang saat ini : {ada['jumlah']}")
                print('Pilih:')
                pilihan = ['Tambah jumlah barang', 'Kurangi jumlah barang']
                tampil_menu_rekursif(pilihan)
                
                while True:
                            tamkur = input('Pilih (1/2): ') 
                            if tamkur in ['1', '2']:
                                break
                            else:
                                print('Pilihan tidak valid!')
                                
                while True:
                    try:
                        jumlah_tamkur = int(input('Masukkan jumlah: '))
                        if jumlah_tamkur <=0:
                            print('Jumlah harus lebih dari 0!')
                            continue
                            
                        if tamkur == '1':
                            ada['jumlah'] += int(jumlah_tamkur) 
                            clear()
                            print('Jumlah barang berhasil ditambahkan!')
                            
                        else:
                            if ada['jumlah'] >= int(jumlah_tamkur): 
                                ada['jumlah'] -= int(jumlah_tamkur)
                                clear()
                                print('Jumlah barang berhasil dikurangi!')
                            else:
                                print('Jumlah terlalu besar untuk dikurangi')
                                continue
                        delay()
                        return
                    except ValueError:
                        print('Harus berupa angka lebih dari 0!')
                        
            elif pilihan_ubah == '3':
                kategori_baru  = input_str('Ubah kategori barang\t:')
                inventaris[k]['kategori'] = kategori_baru
                clear()
                print('Kategori barang berhasil diubah')
                delay()
                return    
            
            elif pilihan_ubah == '4':
                kondisi_baru  = input_str('Ubah kondisi barang\t:')
                inventaris[k]['kondisi'] = kondisi_baru
                print('Kondisi barang berhasil diubah')
                delay()
                return
            
            else:
                print('Pilihan tidak valid!')
                delay()
                return
            
    if not ditemukan:
        print('Kode barang tidak ditemukan')
        delay()
        return
    
def hapus_barang(): #Fungsi menghapus barang
    while True:
        ketemu = False
        clear()
        print('Hapus barang')
        print(daftar())
        
        cari_kode = input_str('Masukkan kode barang yang ingin diubah\t:')
        clear()
        
        
        for l in inventaris:
            if l == cari_kode:
                ketemu = True
                ada = inventaris[l]
                print(f'''Data ditemukan:
Nama\t\t: {ada['nama']}
Kode\t\t: {l}
Jumlah\t\t: {ada['jumlah']}
Kategori\t: {ada['kategori']}
Kondisi\t\t: {ada['kondisi']}''')

                hapus = input('Yakin ingin menghapus barang?(y/n)')
                            
                if hapus.lower() == 'y':
                    inventaris.pop(l)
                    clear()
                    print('Barang berhasil dihapus!')
                    delay()
                    return
                elif hapus.lower() == 'n':
                    print('Penghapusan dibatalkan')
                    delay()
                    return
                else:
                    print('Input tidak valid!')
                    delay()
                    return
                                
        if not ketemu:
            print('Kode barang tidak ditemukan!')
        lagi = input('Ingin hapus barang lagi?(y/n):')
        if lagi.lower() != 'y':
            clear()
            delay()
            return
        clear()

def logout(): #Fungsi log-out dari menu admin/user
    clear()
    kembali = input('Yakin ingin log-out?(y/n):')
    if kembali.lower() == 'y':
        clear()  
        print('Kamu menekan tombol log-out!')
        delay()  
        return True
    elif kembali.lower() == 'n':
        print('Log-out dibatalkan')
        delay()  
        return False
    else:
        print('Pilihan tidak valid!')
        delay()  
        return False
    
    #Tumbal
    print('Tumbal git')