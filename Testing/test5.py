makanan = ["nasi goreng", "sate", "bakso", "mie ayam", "rendang"]  
harga = [12000, 15000, 12000, 15000, 17000]
total = 0
print("Daftar Menu Makanan")
print ("No | Makanan     | Harga")
for i in range(len(makanan)):
    print(f"{i+1:2} | {makanan[i]:11} | Rp {harga[i]:6}")
pilihan = int(input("Masukkan nomor makanan yang ingin dipesan: "))
if 1 <= pilihan <= len(makanan):
    jumlah = int(input("Masukkan jumlah porsi: "))
    total = harga[pilihan - 1] * jumlah
    print(f"Total harga untuk {jumlah} porsi {makanan[pilihan - 1]} adalah Rp {total}")
    if total > 50000:
        diskon = total * 0.10
        total_setelah_diskon = total - diskon
        print(f"Anda mendapatkan diskon 10% sebesar Rp {diskon}")
        print(f"Total yang harus dibayar setelah diskon adalah Rp {total_setelah_diskon}")
    else:
        print("Tidak ada diskon yang diberikan.")
else:
    print("Pilihan tidak valid.")
print("Terima kasih telah memesan di restoran kami!")