print('--- List Harga --- ')
print('Diecast Ukuran 1:64 = Rp 75.000')
print('Diecast Ukuran 1:24 = Rp 150.000')
print('Diecast Ukuran 1:8  = Rp 500.000')
while True:
    smallDiecast = int(input('Masukkan jumlah Diecast Ukuran 1:64 :\t'))
    mediumDiecast = int(input('Masukkan jumlah Diecast Ukuran 1:24 :\t'))
    bigDiecast = int(input('Masukkan jumlah Diecast Ukuran 1:8 :\t'))

    total = (smallDiecast * 75000) + (mediumDiecast * 150000) + (bigDiecast * 500000)

    if total > 1000000:
        diskon = total * 0.10
    elif total > 500000:
        diskon = total * 0.5
    else:
        diskon = 0

    totalAkhir = total - diskon

    print("\n--- Rincian Pembelian ---")
    print(f"Jumlah Diecast Ukuran 1:64\t\t: {bigDiecast}")
    print(f"Jumlah Diecast Ukuran 1:24\t\t: {mediumDiecast}")
    print(f"Jumlah Diecast Ukuran 1:8 \t\t: {smallDiecast}")
    print(f'Total sebelum Diskon\t\t: Rp {total}')
    print(f"Total diskon\t\t\t: Rp {diskon}")
    print(f"Totawl yang harus dibayar\t: Rp {totalAkhir}")

    ulang = input("Apakah ingin membeli lagi?(ya/tidak) ")
    if ulang.lower() != "ya":
        print("Terimakasih telah berbelanja")
        break