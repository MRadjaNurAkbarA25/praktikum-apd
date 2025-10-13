import os
import time
from prettytable import PrettyTable
#Nested list ['Nama barang', 'Kode barang', Jumlah, 'Kategori', 'Kondisi']
inventaris = [
    ['Monitor', '0001', 7, 'Elektronik', 'Baik'], 
    ['Meja kayu', '0002', 10, 'Perabot', 'Baik'],
    ['Buku catatan', '0003', 30,  'Alat tulis', 'Baik'], 
    ['Kursi plastik','0004', 20, 'Perabot', 'Baik'],
    ['Printer', '0005', 5, 'Elektronik', 'Baik'],
    ['Pulpen', '0006', 60,  'Alat tulis', 'Baik']
    ['PC', '0007', 7, 'Elektronik', 'Baik']
]
users = [['radja', '012', 'admin']] #List untuk user
tabel = PrettyTable
tabel.field_names = ['Nama barang', 'Kode', 'Jumlah', 'Kategori', 'Lokasi', 'Kondisi']