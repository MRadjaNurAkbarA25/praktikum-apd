# Praktikum APD Posttest 3 : Percabangan
username = 'radja'
password = '012'
print('''---TOKO CERIA---
Selamat datang di Toko Ceria''')

print('Anda akan mendapat diskon 15% jika bagian dari member kami')
member = input('Apakah anda bagian dari membership?(y/n):')

if member == 'y':
    print('Login Membership')
    username_kamu = input('Username\t:')
    password_kamu = input('Password\t:')

    status_login = True if username == username_kamu and password == password_kamu else False

    if status_login == True:
        print('Login berhasil')
        print('''Daftar barang yang ready hari ini:
1.Sapu\t: Rp. 20.000
2.Ember\t: Rp. 10.000
3.Sikat\t: Rp. 5.000''')
        barang = input('Barang apa yang ingin anda beli?:')

        if barang == '1':
            print('Kamu membeli sapu')
            jumlah = int(input('Berapa banyak barang yang ingin dibeli?:'))
            harga_awal = 20000 * jumlah
            potongan_harga = harga_awal * 0.15
            harga_akhir = harga_awal - potongan_harga
            print(f'''---STRUK BELANJA---
Barang\t        : Sapu
Harga satuan\t: Rp. 20.000/unit
Jumlah\t        : {jumlah}
Harga awal\t: Rp. {harga_awal}
Diskon\t        : 15%
Potongan harga\t: Rp. {potongan_harga}
Harga akhir\t: Rp. {harga_akhir}
---TERIMA KASIH TELAH BERBELANJA---''')

        elif barang == '2':
            print('Kamu membeli ember')
            jumlah = int(input('Berapa banyak barang yang ingin dibeli?:'))
            harga_awal = 10000 * jumlah
            potongan_harga = harga_awal * 0.15
            harga_akhir = harga_awal - potongan_harga
            print(f'''---STRUK BELANJA---
Barang\t        : Ember
Harga satuan\t: Rp. 10.000/unit
Jumlah\t        : {jumlah}
Harga awal\t: Rp. {harga_awal}
Diskon\t        : 15%
Potongan harga\t: Rp. {potongan_harga}
Harga akhir\t: Rp. {harga_akhir}
---TERIMA KASIH TELAH BERBELANJA---''')
        
        elif barang == '3':
            print('Kamu membeli sikat')
            jumlah = int(input('Berapa banyak barang yang ingin dibeli?:'))
            harga_awal = 5000 * jumlah
            potongan_harga = harga_awal * 0.15
            harga_akhir = harga_awal - potongan_harga
            print(f'''---STRUK BELANJA---
Barang\t        : Sikat
Harga satuan\t: Rp. 5.000/unit
Jumlah\t        : {jumlah}
Harga awal\t: Rp. {harga_awal}
Diskon\t        : 15%
Potongan harga\t: Rp. {potongan_harga}
Harga akhir\t: Rp. {harga_akhir}
---TERIMA KASIH TELAH BERBELANJA---''')
        
        else:
            print('Pilihan tidak dalam kategori!')
    else:
        print('Login gagal')

else:
    print('Anda berbelanja sebagai pelanggan biasa!')
    print('''Daftar barang yang ready hari ini:
1.Sapu\t: Rp. 20.000
2.Ember\t: Rp. 10.000
3.Sikat\t: Rp. 5.000''')
    barang = input('Barang apa yang ingin anda beli?:')

    if barang == '1':
        print('Kamu membeli sapu')
        jumlah = int(input('Berapa banyak barang yang ingin dibeli?:'))
        harga_total = 20000 * jumlah
        print(f'''---STRUK BELANJA---
Barang\t        : Sapu
Harga satuan\t: Rp. 20.000/unit            
Jumlah\t        : {jumlah}
Harga total\t: Rp. {harga_total}
---TERIMA KASIH TELAH BERBELANJA---''')

    elif barang == '2':
        print('Kamu membeli ember')
        jumlah = int(input('Berapa banyak barang yang ingin dibeli?:'))
        harga_total = 10000 * jumlah
        print(f'''---STRUK BELANJA---
Barang\t        : Ember
Harga satuan\t: Rp. 10.000/unit            
Jumlah\t        : {jumlah}
Harga total\t: Rp. {harga_total}
---TERIMA KASIH TELAH BERBELANJA---''')

    elif barang == '3':
        print('Kamu membeli sikat')
        jumlah = int(input('Berapa banyak barang yang ingin dibeli?:'))
        harga_total = 5000 * jumlah
        print(f'''---STRUK BELANJA---
Barang\t        : Sikat
Harga satuan\t: Rp. 5.000/unit            
Jumlah\t        : {jumlah}
Harga total\t: Rp. {harga_total}
---TERIMA KASIH TELAH BERBELANJA---''')
    
    else:
        print('Pilihan tidak dalam kategori!')