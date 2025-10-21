import os
import time
from prettytable import PrettyTable
from kamus import inventaris, users

def clear():
    os.system('cls || clear')
    
def delay():
    time.sleep(1)
    
def daftar():
    tabel = PrettyTable ()
    tabel.field_names = ['Kode', 'Nama barang', 'Jumlah', 'Kategori', 'Kondisi']
    print('Daftar barang')
    tabel.clear_rows() 
    for item, data in inventaris.items():
        tabel.add_row([item, data['nama'], data['jumlah'], data['kategori'], data['kondisi'] ])
    return tabel
        
def input_kosong(pesan):
    while True:
        fakta = input(pesan)
        if fakta.strip() != '':
            return fakta
        else:
            print('Input tidak boleh kosong')
            
def keluar():
    os.system('cls || clear')
    while True:
        konfirmasi = input('Yakin ingin keluar dari program?(y/n):')
        
        if konfirmasi.lower() == 'y':
            os.system('cls || clear')
            print('Anda menekan tombol keluar! Terimakasih telah menggunakan program!')
            exit()
        elif konfirmasi.lower() == 'n':
            print('Kembali ke program')
            time.sleep(1)
            os.system('cls || clear')
            return
        else:
            print('Input tidak valid!')


