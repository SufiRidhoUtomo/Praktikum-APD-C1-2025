Sparepart_Khusus_Race = {
    "Suspension" : 450000000,
    "Engine" : 4500000000,
    "Turbocharger" : 1200000000,
    "Exhaust" : 350000000,
    "Brake System" : 1200000000,
    "Steering Wheel" : 250000000,
    "Tire" : 200000000,
    "Racing Seat" : 300000000,
    "Clutch" : 350000000,
    "Gearbox" : 4000000000,
    "Fuel System" :  250000000,
    "Cooling System" : 200000000,
    "Ignition System" : 400000000,
    "Carbon Body Kit" : 1500000000,
    "Aerodynamics Kit" : 750000000,
    "Lightweight Wheels" : 600000000,
    "Performance Chip" : 200000000,
    "High-Performance Battery" : 60000000,
    "Racing Harness" : 40000000,   
    "Data Logger" : 500000000,
    "Roll Cage" : 300000000,
    "Fire Suppression System" : 100000000,
    "Racing Fuel" : 30000000,
    "Performance Oil" : 2500000,
    "Brake Pads" : 25000000,
    "Air Filter" : 6000000,
    "Spark Plugs" : 6000000,
    "Clutch Kit" : 350000000,
    "Lightweight Flywheel" : 80000000,
    "Short Shifter" : 120000000,
    "Strut Bar" : 25000000,
    "Sway Bars" : 30000000,
    "Camber Kits" : 30000000,

}
print("Daftar Sparepart Toko Max")
print("No | Nama Sparepart_Khusus,Race | Harga Satuan")
print("------------------------------------------------")
print("1  | Suspension               | 450.000.000")
print("2  | Engine                   | 4.500.000.000")
print("3  | Turbocharger             | 1.200.000.000")
print("4  | Exhaust                  | 350.000.000")
print("5  | Brake System             | 1.200.000.000")
print("6  | Steering Wheel           | 250.000.000")
print("7  | Tire                     | 200.000.000")
print("8  | Racing Seat              | 300.000.000")
print("9  | Clutch                   | 350.000.000")
print("10 | Gearbox                  | 4.000.000.000")
print("11 | Fuel System              | 250.000.000")
print("12 | Cooling System           | 200.000.000")
print("13 | Ignition System          | 400.000.000")
print("14 | Carbon Body Kit          | 1.500.000.000")
print("15 | Aerodynamics Kit         | 750.000.000")
print("16 | Lightweight Wheels       | 600.000.000")
print("17 | Performance Chip         | 200.000.000")
print("18 | High-Performance Battery | 60.000.000")
print("19 | Racing Harness           | 40.000.000")
print("20 | Data Logger              | 500.000.000")
print("21 | Roll Cage                | 300.000.000")
print("22 | Fire Suppression System  | 100.000.000")
print("23 | Racing Fuel              | 30.000.000")
print("24 | Performance Oil          | 2.500.000")
print("25 | Brake Pads               | 25.000.000")
print("26 | Air Filter               | 6.000.000")
print("27 | Spark Plugs              | 6.000.000")
print("28 | Clutch Kit               | 350.000.000")
print("29 | Lightweight Flywheel     | 80.000.000")
print("30 | Short Shifter            | 120.000.000")
print("31 | Strut Bar                | 25.000.000")
print("32 | Sway Bars                | 30.000.000")
print("33 | Camber Kits              | 30.000.000")
print("------------------------------------------------")

pesananan = []

while True :
    pilihan = input("pilih Nomor Sparepart yang ingin di beli (ketik 'selesai' untuk melakukan pembayaran): ")
    if pilihan.lower() == "selesai":
        break
    if not pilihan.isdigit() or int(pilihan) < 1 or int(pilihan) > len(Sparepart_Khusus_Race):
        print("Pilihan tidak valid. Coba lagi.")
        continue
    nomor = int(pilihan)
    nama_sparepart = list(Sparepart_Khusus_Race.keys())[nomor - 1]
    harga_sparepart = Sparepart_Khusus_Race[nama_sparepart]
    pesananan.append((nama_sparepart, harga_sparepart))
    print(f"{nama_sparepart} telah ditambahkan ke pesanan Anda.")
total_harga = sum(harga for _, harga in pesananan)
print("\nRincian Pesanan Anda:")
for nama, harga in pesananan:
    print(f"- {nama}: {harga:,}")
print(f"Total Harga: {total_harga:,}")
print("Terima kasih telah berbelanja di Toko Max!")
