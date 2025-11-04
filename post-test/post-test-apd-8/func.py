import os
import time
from prettytable import PrettyTable
from kamus import inventaris, users
from colorama import Fore, Back, Style, init

init(autoreset=True)

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
    print(Fore.GREEN + f'{index + 1}. {menu_list[index]}')
    tampil_menu_rekursif(menu_list, index + 1)

def input_str(pesan): #Fungsi error handling untuk mencegah input kosong
    while True:
        try:
            fakta = input(pesan)
            if fakta.strip() == '':
                raise ValueError(Fore.RED + Style.BRIGHT + 'Input tidak boleh kosong!')
            return fakta
        except ValueError as e:
            print(e)  

def regist_pw(pesan): #Fungsi error handling untuk memasukkan password akun baru(registrasi)
    while True: #
        try:
            pw_baru = input(pesan)
            if len(pw_baru) < 3:
                raise ValueError(Fore.RED + Style.BRIGHT + 'Password minimal 3 karakter!')
            return pw_baru
        except ValueError as e:
            print(e)

def jumlah(pesan): #Fungsi error handling untuk menginput jumlah dari opsi menambah barang baru
    while True:
        try:
            jumlah_input = input(pesan)
            if jumlah_input.strip() == '':
                raise ValueError(Fore.RED + Style.BRIGHT + 'Input tidak boleh kosong!')
            jumlah_int = int(jumlah_input)
            if jumlah_int <= 0:
                raise ValueError(Fore.RED + Style.BRIGHT + 'Jumlah harus lebih besar dari 0!')
            return jumlah_int
        except ValueError:
            if jumlah_input.strip() == '':
                print('Input tidak boleh kosong!')
            else:
                try:
                    if int(jumlah_input) <= 0:
                        print('Jumlah harus lebih besar dari 0!')
                except:
                    print(Fore.RED + Style.BRIGHT + 'Input harus berupa angka!')

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
        print(Fore.RED + Style.BRIGHT + 'Pilihan tidak valid!')
        delay()  
        return False

def keluar(): #Fungsi untuk keluar dari program
    clear()
    while True:
        konfirmasi = input('Yakin ingin keluar dari program?(y/n):')
        
        if konfirmasi.lower() == 'y':
            clear()
            print(Fore.BLUE + 'Anda menekan tombol keluar! Terimakasih telah menggunakan program!')
            delay()
            exit()
        elif konfirmasi.lower() == 'n':
            print('Kembali ke program')
            delay()
            clear()
            return
        else:
            print(Fore.RED + Style.BRIGHT + 'Input tidak valid!') 
            
