# Program Diskon Laptop:

# Nama : Sufi Ridho Utomo
# NIM : 2509106101
# Kelas : Informatika C1'25

# Besaran Diskon Laptop
Lenovo = 0.10
Asus = 0.07
Acer = 0.05

# Input Data Pembeli
Nama = str(input("Nama Lengkap : "))
NIM = int(input("NIM : "))
Harga = int(input("Harga : Rp."))
print(" ")
print("    ==Data Pembeli==")
print("-> |Nama : ", Nama)
print("-> |NIM : ", NIM)
print("-> |Harga : Rp.", Harga)

# Menghitung Diskon
Diskon_Lenovo = int(Harga*(Lenovo))
Diskon_Asus = int(Harga*(Asus))
Diskon_Acer = int(Harga*(Acer))
print(" ")
print("       ==Besar Diskon==")
print("Diskon Laptop Lenovo : Rp.",Diskon_Lenovo)
print("Diskon Laptop Asus : Rp.",Diskon_Asus)
print("Diskon Laptop Acer : Rp.",Diskon_Acer)

# Hasil Akhir Diskon
Harga_Lenovo = int(Harga - Diskon_Lenovo)
Harga_Asus = int(Harga - Diskon_Asus)
Harga_Acer = int(Harga - Diskon_Acer)
print(" ")
print("       ==Harga Diskon==")
print("Harga Laptop Lenovo : Rp.",Harga_Lenovo)
print("Harga Laptop Asus : Rp.",Harga_Asus)
print("Harga Laptop Acer : Rp.",Harga_Acer)
