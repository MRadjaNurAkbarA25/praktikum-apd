import os, time
from prettytable import PrettyTable
from kamus import inventaris, users
import necfunc as sip

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
                usr = sip.input_kosong('Masukkan Username\t:')
                pw = sip.input_kosong('Masukkan password\t:')
                
                for u in users:
                    if usr == u and pw == users[u]['password']:
                        role = users[u]['role']
                        loginn = True
                        break
                if loginn:
                    sip.clear()
                    print('Login berhasil!')
                    sip.delay(1)
                    break
                else:
                    sip.clear()
                    print('Username atau password salah!')
            if loginn:
                break
            
        elif menu == '2':
            sip.clear()
            print('Registrasi')
            
            while True:
                cek_ada_usr = False
                usr_baru = sip.input_kosong('Masukkan Username baru\t:')
                
                for u in users: 
                    if usr_baru == u:
                        cek_ada_usr = True
                        break
                    
                if cek_ada_usr:
                    print('Username sudah terpakai! Gunakan Username lain')
                else:
                    while True:
                        pw_baru = input('Masukkan password\t:')
                        if len(pw_baru) < 3:
                            print('Password minimal berjumlah 3 karakter!')
                        else: 
                            break
                    users.update({
                        usr_baru : {'password' : pw_baru, 
                                    'role' : 'user' 
                        }
                    })
                    sip.clear()
                    print('Registrasi berhasil!')
                    break
            
        elif menu == '3':
            sip.keluar()
            
        else:
            os.system('cls || clear')
            print('Input tidak valid!')

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
            
            if menu_admin == '1':
                sip.clear()
                print(sip.daftar())
                
            elif menu_admin == '2':

                sip.clear()
                print('Tambah barang')
                
                nama_barang = sip.input_kosong('Nama barang\t:')
                
                while True:
                    cek_kode_barang = False
                    kode_barang = sip.input_kosong('Kode barang\t:')
                    
                    for j in inventaris:
                        if kode_barang == j:
                            cek_kode_barang = True
                            break
                    if cek_kode_barang:
                        print('Kode barang sudah terpakai! Gunakan kode lain!')
                    else:
                        break
                
                while True:
                        jumlah_input = input('Jumlah barang\t:') 
                        if jumlah_input.isdigit() and int(jumlah_input) > 0: 
                            jumlah_barang = int(jumlah_input)
                            break
                        else:
                            print('Jumlah harus tidak boleh kosong dan harus berupa angka lebih dari 0!')
                            
                kategori_barang = sip.input_kosong('Kategori barang\t:')
                
                kondisi_barang = sip.input_kosong('Kondisi barang\t:')
                
                inventaris.update({
                    kode_barang : {'nama' : nama_barang,
                                'jumlah' : jumlah_barang,
                                'kategori' : kategori_barang,
                                'kondisi' : kondisi_barang}
                })
                sip.clear()
                print('Barang berhasil ditambahkan!')

            elif menu_admin == '3':
                ditemukan = False
                sip.clear()
                print('Ubah data barang')
                print(sip.daftar())
                
                cari_kode = sip.input_kosong('Masukkan kode barang yang ingin diubah\t:')
                sip.clear()
                
                
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

                        print('''Pilih data yang ingin diubah:
1. Ubah nama barang
2. Ubah jumlah barang
3. Ubah kategori
4. Ubah kondisi''')
                        pilihan_ubah = input('Pilih apa yang ingin diubah: ')
                        
                        if pilihan_ubah == '1':
                            nama_baru = sip.input_kosong('Ubah nama barang\t:')
                            inventaris[k]['nama'] = nama_baru
                            sip.clear()
                            print('Nama barang berhasil diubah')
                            break
                        
                        elif pilihan_ubah == '2':
                            sip.clear()
                            print(f"Jumlah barang saat ini : {ada['jumlah']}")
                            print('''Pilih:
1. Tambah jumlah barang
2. Kurangi jumlah barang''')
                            
                            while True:
                                tamkur = input('Pilih (1/2): ') 
                                if tamkur in ['1', '2']:
                                    break
                                else:
                                    print('Pilihan tidak valid!')
                                    
                            while True:
                                jumlah_tamkur = input('Masukkan jumlah: ')
                                if jumlah_tamkur.isdigit() and int(jumlah_tamkur) > 0: 
                                    proses_operasional = int(jumlah_tamkur) 
                                    
                                    if tamkur == '1':
                                        ada['jumlah'] += proses_operasional 
                                        sip.clear()
                                        print('Jumlah barang berhasil ditambahkan!')
                                        break
                                    
                                    elif tamkur == '2':
                                        if ada['jumlah'] >= proses_operasional: 
                                            ada['jumlah'] -= proses_operasional
                                            sip.clear()
                                            print('Jumlah barang berhasil dikurangi!')
                                            break
                                        else:
                                            print('Jumlah terlalu besar untuk dikurangi')
                                else:
                                    print('Harus berupa angka lebih dari 0!')
                                    
                        elif pilihan_ubah == '3':
                            kategori_baru  = sip.input_kosong('Ubah kategori barang\t:')
                            inventaris[k]['kategori'] = kategori_baru
                            sip.clear()
                            print('Kategori barang berhasil diubah')
                            break
                            
                        elif pilihan_ubah == '4':
                            kondisi_baru  = sip.input_kosong('Ubah kondisi barang\t:')
                            inventaris[k]['kondisi'] = kondisi_baru
                            print('Kondisi barang berhasil diubah')
                            break
                if not ditemukan:
                    sip.clear()
                    print('Kode barang tidak ditemukan')
                    
            elif menu_admin == '4':
                sip.clear()
                print('Hapus barang')
                
                while True:
                    ketemu = False
                    print(sip.daftar())
                    
                    cari_kode_hapus = sip.input_kosong('Masukkan kode barang yang ingin dihapus\t:')
                    
                    for l in inventaris:
                        if l == cari_kode_hapus:
                            ketemu = True
                            ama = inventaris[l]
                            print(f'''
    Data ditemukan:
    Nama\t\t: {ama['nama']}
    Kode\t\t: {l}
    Jumlah\t\t: {ama['jumlah']}
    Kategori\t: {ama['kategori']}
    Kondisi\t\t: {ama['kondisi']}''')
                            hapus = input('Yakin ingin menghapus barang?(y/n)')
                            
                            if hapus.lower() == 'y':
                                inventaris.pop(l)
                                sip.clear()
                                print('Barang berhasil dihapus!')
                                break
                            elif hapus.lower() == 'n':
                                print('Penghapusan dibatalkan')
                                break
                            else:
                                print('Input tidak valid!')
                                break
                                
                    if not ketemu:
                        print('Kode barang tidak ditemukan!')
                    lagi = input('Ingin hapus barang lagi?(y/n):')
                    if lagi.lower() != 'y':
                        sip.clear()
                        break
                    sip.clear()                    
            
            elif menu_admin == '5':
                sip.clear()
                kembali1 = input('Yakin ingin log-out?(y/n): ')
                if kembali1.lower() == 'y':
                    os.system('cls || clear')
                    print('Kamu menekan tombol log-out!')
                    break
                elif kembali1.lower() == 'n':
                    print('Log-out dibatalkan')
                else:
                    print('Pilihan tidak valid!')
                    
            elif menu_admin == '6':
                sip.keluar()
            
            else:
                sip.clear()
                print('Input tidak valid!')
            
        else:
            print(f'Halo, {usr}!')
            print('''===MENU USER===
1. Lihat barang
2. Log-out
3. Keluar''')
            menu_user = input('Pilih menu: ')
            
            if menu_user == '1':
                sip.clear()
                print('Daftar barang')
                print(sip.daftar())
                
            elif menu_user == '2':
                sip.clear()
                kembali2 = input('Yakin ingin log-out?(y/n): ')
                if kembali2.lower() == 'y':
                    os.system('cls || clear')
                    print('Kamu menekan tombol log-out!')
                    break
                elif kembali2.lower() == 'n':
                    print('Log-out dibatalkan')
                else:
                    print('Pilihan tidak valid!')
                    
            else:
                sip.keluar()