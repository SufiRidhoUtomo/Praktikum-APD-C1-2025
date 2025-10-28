bahan = ["semen", "batu bata", "pasir", "besi"]
jumlah = [100, 200, 300, 400]
harga = [10000, 5000, 20000, 15000]
total = 0
print("Daftar Bahan Bangunan")
print("No | Bahan       | Jumlah | Harga Satuan | Total Harga")
for i in range(len(bahan)):
    total_harga = jumlah[i] * harga[i]
    total += total_harga
    print(f"{i+1:2} | {bahan[i]:11} | {jumlah[i]:6} | Rp {harga[i]:12} | Rp {total_harga:11}")
print(f"Total Keseluruhan Harga: Rp {total}")
if total > 1000000:
    diskon = total * 0.10
    total_setelah_diskon = total - diskon
    print(f"Diskon 10%: Rp {diskon}")
    print(f"Total Setelah Diskon: Rp {total_setelah_diskon}")
elif total > 500000:
    diskon = total * 0.05
    total_setelah_diskon = total - diskon
    print(f"Diskon 5%: Rp {diskon}")
    print(f"Total Setelah Diskon: Rp {total_setelah_diskon}")
else:
    print("Tidak ada diskon yang diberikan.")
print("Terima kasih telah berbelanja di toko kami!")
