import func as fu
from prettytable import PrettyTable
from kamus import inventaris, users
from colorama import Fore, Back, Style, init

init(autoreset=True)

def login(): #Fungsi untuk login
    fu.clear()
    print(Fore.WHITE + 'Login akun')
    while True:
        #Variabel lokal
        usr = fu.input_str('Masukkan Username\t:') 
        pw = fu.input_str('Masukkan password\t:')
        
        for u in users:
            if usr == u and pw == users[u]['password']:
                role = users[u]['role']
                fu.clear()
                print(Fore.GREEN + Style.BRIGHT + 'Login berhasil!')
                fu.delay()
                return usr, role
            else:
                fu.clear()
                print(Fore.RED + Style.BRIGHT + 'Username atau passsword salah!')

def register(): #Fungsi untuk registrasi
    fu.clear()
    print(Fore.BLACK + 'Registrasi')
    while True:
        cek_ada_usr = False
        usr_baru = fu.input_str('Masukkan username baru:')
        
        for u in users:
            if usr_baru == u:
                cek_ada_usr = True
                break
        if cek_ada_usr:
            print(Fore.RED + Style.BRIGHT + 'Username sudah terpakai! Gunakan username lain')
        else:
            pw_baru = fu.regist_pw('Masukkan password:')
            users.update({
                        usr_baru : {'password' : pw_baru, 
                                    'role' : 'user' 
                        }
                    })
            fu.clear()
            print(Fore.GREEN + Style.BRIGHT +'Registrasi berhasil!')
            fu.delay()
            return usr_baru, pw_baru