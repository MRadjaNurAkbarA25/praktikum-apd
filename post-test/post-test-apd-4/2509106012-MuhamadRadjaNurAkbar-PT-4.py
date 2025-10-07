# Perulangan
import os

usr = 'radja'
pw = '012'

print('''---TOKO CERIA---
Selamat datang di Toko Ceria''')
print('Anda akan mendapat diskon 15% jika bagian dari member kami')

# Logika Login
while True:
    keranjang = ''
    total = 0
    loginn = False
    member = input('Apakah anda bagian dari membership?(y/n):')
    
    if member == 'y':
        hitung = 3
        while hitung > 0:
            username = input('Username\t:')
            password = input('Password\t:')
            if username == '' or password == '':
                print('Username dan Password tidak boleh kosong!')
                continue
            if username == usr and password == pw:
                loginn = True
                break
            else:
                print('Username atau Password salah!')
                hitung -= 1
                print(f'Sisa kesempatan login: {hitung}')
        if hitung == 0:
            print('Kesempatan login telah habis! Anda berbelanja sebagai pelanggan biasa')

    elif member == 'n':
        print('Anda berbelanja sebagai pelanggan biasa')

    else:
        print('Anda berbelanja sebagai pelanggan biasa')

    # Logika belanja
    while True:
        print('=' * 39)
        print('|No          |Barang      |Harga(Rp)  |')
        print('-' * 39)
        print('|1           |Sapu        |20.000     |')
        print('|2           |Ember       |10.000     |')
        print('|3           |Sikat       |5.000      |')
        print('-' * 39)
        print('|4           |Checkout    |           |')
        print('=' * 39)
        pilihan = int(input('Pilih (1-4):'))

        if pilihan == 1:
            keranjang += 'Sapu\t:20.000\n'
            total += 20000
            os.system('cls')
            print('Sapu dimasukkan ke keranjang')
            print(f'Total sementara: {total}')
        elif pilihan == 2:
            keranjang += 'Ember\t:10.000\n'
            total += 10000
            os.system('cls')
            print('Ember dimasukkan ke keranjang')
            print(f'Total sementara: {total}')
        elif pilihan == 3:
            keranjang += 'Sikat\t:5.000\n'
            total += 5000
            os.system('cls')
            print('Sikat dimasukkan ke keranjang')
            print(f'Total sementara: {total}')
        elif pilihan == 4:
            os.system('cls')
            print('=' * 19)
            print('---STRUK BELANJA---')
            print('=' * 19)
            print(f'{keranjang}')

            if loginn: #Jika Member
                potongan_harga = total * 0.15
                harga_akhir = total - potongan_harga
                print(f'Harga Asli\t: Rp. {total:,}')
                print(f'Diskon Member\t: (15%): Rp. -{potongan_harga:,}')
                print(f'Total\t        : Rp. {harga_akhir:,}')
                break
            else: #Non-Member
                print(f'Total\t        : Rp. {total:,}')
                print('---TERIMA KASIH TELAH BERBELANJA---')
                break
        else:
            os.system('cls')
            print('Input tidak valid!')

#Logika Konfirmasi
    while True:
        ulang = input('Ingin memulai transaksi baru?(y/n):')
        if ulang == 'y':
            break
        elif ulang == 'n':
            print('Terima kasih telah berbelanja!')
            break
        else:
            print('Input tidak valid')

    if ulang == 'n':
        break

