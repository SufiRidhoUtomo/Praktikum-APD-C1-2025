#list harga masing - masing ukuran diecast
print('---list harga---')
print("Diecast 1:8 = Rp. 500.000")
print(" Diecast 1:24 = Rp. 150.000")
print('Diecast 1:64 = Rp. 75.000')

#menentukan harga dari masing masing diecast

big_diecast = 500000
med_diecast = 150000
small_diecast = 75000

total = 0


while True:
    beli_big_diecast = int(input("Mau berapa big diecast bang??"))
    beli_med_diecast = int(input("Mau berapa med diecast bang??"))
    beli_small_diecast = int(input("Mau berapa small diecast bang??"))

    total = (beli_big_diecast*big_diecast) + (beli_med_diecast*med_diecast) + (beli_small_diecast*small_diecast)

    if total > 1000000:
        total = total - (total*0.10)
        print("total belanjaan adalah ", total)

    elif total >500000:
        total = total-(total*0.05)
        print("total belanjaan adalah", total)

    else :
        print("total belanjaan adalah", total)
    
    ulangin = input("apakah anda ingin melakukan pembelian lagi? (ya atau tidak)") 
    if ulangin != "ya":
        print("Terima kasih silahkan datang kembali ")
        break 

