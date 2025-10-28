from prettytable import PrettyTable
from kamus import inventaris, users
import function as sip
import os, time

while True: #Loop utama program
    #Variabel global
    role = None
    loginn = False
    while True:
        print('===Menu===')
        menu_utama = ['Login', 'Registrasi', 'Keluar']
        sip.tampil_menu_rekursif(menu_utama)
        
        menu = input('Pilih menu:')
        
        if menu == '1':
            usr, role = sip.login()
            loginn = True
            break
        elif menu == '2':
            print('Registrasi')
            usr_baru, pw_baru  = sip.register()
            sip.clear()
            continue
        elif menu == '3':
            sip.keluar()
        else:
            print('Input tidak valid!')
    log_out = False
    
    while True:
        if role == 'admin': #Menu admin
            print(f'Halo, {usr}!')
            
            print('===MENU ADMIN===')
            menu_utama_admin = ['Lihat barang', 'Tambah barang', 'Ubah data barang',
                                'Hapus barang', 'Log-out', 'Keluar']
            sip.tampil_menu_rekursif(menu_utama_admin)
            
            menu_admin = input('Pilih menu:')
            
            if menu_admin == '1':
                sip.clear()
                print('Lihat barang')
                print(sip.daftar())
                
            elif menu_admin == '2':
                sip.clear()
                print('Tambah barang')
                sip.tambah_barang()
                
            elif menu_admin == '3':
                sip.clear()
                print('Ubah data barang')
                sip.ubah_data()
            
            elif menu_admin == '4':
                sip.clear()
                print('Hapus barang')
                sip.hapus_barang()
                
            elif menu_admin == '5':
                if sip.logout():
                    log_out = True
                    break
                
            elif menu_admin == '6':
                sip.clear()
                sip.keluar()
            
            else:
                sip.clear()
                print('Input tidak valid!')
            continue        
        if log_out:
            break
        
        else:
            print(f'Halo, {usr}!')
            print('===MENU USER===')
            
            menu_utama_user = ['Lihat barang', 'Log-out', 'Keluar']
            sip.tampil_menu_rekursif(menu_utama_user)

            menu_user = input('Pilih menu: ')
            
            if menu_user == '1':
                sip.clear()
                print('Lihat barang')
                print(sip.daftar())
            elif menu_user == '2':
                if sip.logout():
                    log_out = True
                    break
            elif menu_user == '3':
                sip.clear()
                sip.keluar()    
            else:
                print('Input tidak valid!')
        if log_out:
            break