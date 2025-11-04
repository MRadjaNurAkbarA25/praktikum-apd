from prettytable import PrettyTable
from kamus import inventaris, users
from colorama import Fore, Back, Style, init
import func as fu
import mainmenu as maimu
import menurole as rol

init(autoreset=True)

while True: #Loop utama program
    #Variabel global
    role = None
    loginn = False
    while True:
        print(Fore.GREEN + '===Menu===')
        menu_utama = ['Login', 'Registrasi', 'Keluar']
        fu.tampil_menu_rekursif(menu_utama)
        
        menu = input(Fore.CYAN + 'Pilih menu:')
        
        if menu == '1':
            usr, role = maimu.login()
            loginn = True
            break
        elif menu == '2':
            usr_baru, pw_baru  = maimu.register()
            fu.clear()
            continue
        elif menu == '3':
            fu.keluar()
        else:
            print(Fore.RED + Style.BRIGHT + 'Input tidak valid!')
    log_out = False
    
    while True:
        if role == 'admin': #Menu admin
            print(Fore.BLUE + f'Halo, {usr}!')
            
            print(Fore.GREEN + '===MENU ADMIN===')
            menu_utama_admin = ['Lihat barang', 'Tambah barang', 'Ubah data barang',
                                'Hapus barang', 'Log-out', 'Keluar']
            fu.tampil_menu_rekursif(menu_utama_admin)
            
            menu_admin = input(Fore.CYAN + 'Pilih menu:')
            
            if menu_admin == '1':
                fu.clear()
                print(Fore.YELLOW + 'Lihat barang')
                print(fu.daftar())
                
            elif menu_admin == '2':
                fu.clear()
                print(Fore.YELLOW + 'Tambah barang')
                rol.tambah_barang()
                
            elif menu_admin == '3':
                fu.clear()
                print(Fore.YELLOW + 'Ubah data barang')
                rol.ubah_data()
            
            elif menu_admin == '4':
                fu.clear()
                print(Fore.YELLOW + 'Hapus barang')
                rol.hapus_barang()
                
            elif menu_admin == '5':
                if fu.logout():
                    log_out = True
                    break
                
            elif menu_admin == '6':
                fu.clear()
                fu.keluar()
            
            else:
                fu.clear()
                print(Fore.RED + Style.BRIGHT + 'Input tidak valid!')
            continue        
        if log_out:
            break
        
        else:
            print(Fore.BLUE + f'Halo, {usr}!')
            print(Fore.GREEN + '===MENU USER===')
            
            menu_utama_user = ['Lihat barang', 'Log-out', 'Keluar']
            fu.tampil_menu_rekursif(menu_utama_user)

            menu_user = input(Fore.CYAN + 'Pilih menu: ')
            
            if menu_user == '1':
                fu.clear()
                print(Fore.YELLOW + 'Lihat barang')
                print(fu.daftar())
            elif menu_user == '2':
                if fu.logout():
                    log_out = True
                    break
            elif menu_user == '3':
                fu.clear()
                fu.keluar()    
            else:
                print(Fore.RED + Style.BRIGHT + 'Input tidak valid!')
        if log_out:
            break