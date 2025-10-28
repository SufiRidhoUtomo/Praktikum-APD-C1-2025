# Daftar menu makanan
menu = [
    {"nama": "Nasi Goreng", "harga": 20000},
    {"nama": "Mie Ayam", "harga": 18000},
    {"nama": "Sate Ayam", "harga": 25000},
    {"nama": "Bakso", "harga": 22000},
    {"nama": "Es Teh", "harga": 5000},
    {"nama": "Jus Alpukat", "harga": 10000}
]

# Menampilkan menu
print("=== MENU RESTORAN ===")
for i, item in enumerate(menu):
    print(f"{i+1}. {item['nama']} - Rp{item['harga']}")

# List untuk menyimpan pesanan
pesanan = []

# Perulangan untuk memilih menu
while True:
    pilihan = input("Pilih nomor menu (atau ketik 'selesai' untuk mengakhiri): ")
    if pilihan.lower() == "selesai":
        break
    if not pilihan.isdigit() or int(pilihan) < 1 or int(pilihan) > len(menu):
        print("Pilihan tidak valid. Coba lagi.")
        continue
    pesanan.append(menu[int(pilihan)-1])
    print(f"{menu[int(pilihan)-1]['nama']} ditambahkan ke pesanan.")

# Menampilkan ringkasan pesanan
print("\n=== RINGKASAN PESANAN ===")
total = 0
for item in pesanan:
    print(f"- {item['nama']} : Rp{item['harga']}")
    total += item['harga']

# Percabangan untuk diskon
if total >= 100000:
    diskon = total * 0.1
    print(f"Diskon 10%: -Rp{int(diskon)}")
    total -= diskon
elif total >= 50000:
    diskon = total * 0.05
    print(f"Diskon 5%: -Rp{int(diskon)}")
    total -= diskon
else:
    print("Tidak ada diskon.")

print(f"Total yang harus dibayar: Rp{int(total)}")
print("Terima kasih telah memesan!")
