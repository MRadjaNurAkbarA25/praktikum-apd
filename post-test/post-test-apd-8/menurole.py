from prettytable import PrettyTable
import func as fu
import mainmenu as maimu
from kamus import inventaris, users
from colorama import Fore, Back, Style, init

init(autoreset=True)

#Contoh prosedur
def tambah_barang(): #Fungsi untuk menambah barang baru ke daftar barang
    while True:
        nama_barang = fu.input_str('Nama barang:')
        
        while True:
            cek_kode = False
            kode_barang = fu.input_str('Kode barang:')
                    
            for j in inventaris:
                if kode_barang == j:
                    cek_kode = True
                    break
            if cek_kode:
                print(Fore.RED + Style.BRIGHT + 'Kode barang sudah terpakai! Gunakan kode lain!')
            else:
                break
                
        jumlah_barang = fu.jumlah('Jumlah barang:')
        
        kategori_barang = fu.input_str('Kategori barang\t:')
                
        kondisi_barang = fu.input_str('Kondisi barang\t:')
        
        inventaris.update({
            kode_barang : {'nama' : nama_barang,
                        'jumlah' : jumlah_barang,
                        'kategori' : kategori_barang,
                        'kondisi' : kondisi_barang}
        })
        
        fu.clear()
        print(Fore.GREEN + Style.BRIGHT + 'Barang berhasil ditambahkan!')
        fu.delay()
        return

def ubah_data(): #Fungsi mengubah data barang yang sudah ada
    ditemukan = False
    fu.clear()
    print('Ubah data barang')
    print(fu.daftar())
    
    cari_kode = fu.input_str('Masukkan kode barang yang ingin diubah\t:')
    fu.clear()
    
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
            fu.tampil_menu_rekursif(menu_ubah_barang)
            
            pilihan_ubah = input('Pilih apa yang ingin diubah: ')
            
            if pilihan_ubah == '1':
                nama_baru = fu.input_str('Ubah nama barang:')
                inventaris[k]['nama'] = nama_baru   
                fu.clear()
                print(Fore.GREEN + Style.BRIGHT + 'Nama berhasil diubah!')
                fu.delay()
                return
            
            if pilihan_ubah == '2':
                fu.clear()
                
                print(f"Jumlah barang saat ini : {ada['jumlah']}")
                print('Pilih:')
                pilihan = ['Tambah jumlah barang', 'Kurangi jumlah barang']
                fu.tampil_menu_rekursif(pilihan)
                
                while True:
                            tamkur = input('Pilih (1/2): ') 
                            if tamkur in ['1', '2']:
                                break
                            else:
                                print(Fore.RED + Style.BRIGHT + 'Pilihan tidak valid!')
                                
                while True:
                    try:
                        jumlah_tamkur = int(input('Masukkan jumlah: '))
                        if jumlah_tamkur <=0:
                            print(Fore.RED + Style.BRIGHT + 'Jumlah harus lebih dari 0!')
                            continue
                            
                        if tamkur == '1':
                            ada['jumlah'] += int(jumlah_tamkur) 
                            fu.clear()
                            print(Fore.GREEN + Style.BRIGHT + 'Jumlah barang berhasil ditambahkan!')
                            
                        else:
                            if ada['jumlah'] >= int(jumlah_tamkur): 
                                ada['jumlah'] -= int(jumlah_tamkur)
                                fu.clear()
                                print(Fore.GREEN + Style.BRIGHT + 'Jumlah barang berhasil dikurangi!')
                            else:
                                print(Fore.RED + Style.BRIGHT + 'Jumlah terlalu besar untuk dikurangi')
                                continue
                        fu.delay()
                        return
                    except ValueError:
                        print(Fore.RED + Style.BRIGHT + 'Harus berupa angka lebih dari 0!')
                        
            elif pilihan_ubah == '3':
                kategori_baru  = fu.input_str('Ubah kategori barang\t:')
                inventaris[k]['kategori'] = kategori_baru
                fu.clear()
                print(Fore.GREEN + Style.BRIGHT + 'Kategori barang berhasil diubah!')
                fu.delay()
                return    
            
            elif pilihan_ubah == '4':
                kondisi_baru  = fu.input_str('Ubah kondisi barang\t:')
                inventaris[k]['kondisi'] = kondisi_baru
                print(Fore.GREEN + Style.BRIGHT + 'Kondisi barang berhasil diubah!')
                fu.delay()
                return
            
            else:
                print(Fore.RED + Style.BRIGHT + 'Input tidak valid!')
                fu.delay()
                return
            
    if not ditemukan:
        print(Fore.RED + Style.BRIGHT + 'Kode barang tidak ditemukan!')
        fu.delay()
        return
    
def hapus_barang(): #Fungsi menghapus barang
    while True:
        ketemu = False
        fu.clear()
        print('Hapus barang')
        print(fu.daftar())
        
        cari_kode = fu.input_str('Masukkan kode barang yang ingin diubah\t:')
        fu.clear()
        
        
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
                    fu.clear()
                    print('Barang berhasil dihapus!')
                    fu.delay()
                    return
                elif hapus.lower() == 'n':
                    print('Penghapusan dibatalkan')
                    fu.delay()
                    return
                else:
                    print(Fore.RED + Style.BRIGHT + 'Input tidak valid!')
                    fu.delay()
                    return
                                
        if not ketemu:
            print(Fore.RED + Style.BRIGHT + 'Kode barang tidak ditemukan!')
        lagi = input('Ingin hapus barang lagi?(y/n):')
        if lagi.lower() != 'y':
            fu.clear()
            fu.delay()
            return
        fu.clear()