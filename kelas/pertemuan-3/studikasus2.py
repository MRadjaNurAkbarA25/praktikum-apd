belanja = float(input('Masukkan total belanja anda:'))

if belanja > 100000:
    diskon = belanja * 0.2
    totalBayar = belanja - diskon
    print('Diskon 20 persen')
    print(f'Potongan harga\t : Rp {diskon}')
    print(f'Total bayar\t : Rp {totalBayar}')
elif belanja > 50000:
    diskon = belanja * 0.1
    totalBayar = belanja - diskon
    print('Diskon 10 persen')
    print(f'Potongan harga\t : Rp {diskon}')
    print(f'Total bayar\t : Rp {totalBayar}')
else:
    print('Gak dapat diskon') 