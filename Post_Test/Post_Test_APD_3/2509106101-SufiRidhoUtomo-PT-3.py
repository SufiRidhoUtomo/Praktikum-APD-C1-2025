#SOAL NIM Ganjil
#Buatlah program Python untuk menghitung pembayaran biaya langganan aplikasi streaming musik senilai Rp 1.500.000. Program harus memenuhi ketentuan berikut:

#1. Validasi Login:
#Pengguna harus memasukkan nama dan NIM yang sesuai dengan data diri Anda.
#Jika login gagal, program tidak akan menampilkan menu pembayaran.
#Jika login berhasil, program menampilkan opsi pembayaran biaya langganan aplikasi streaming musik.
#2. Opsi Pembayaran Biaya Langganan Aplikasi Streaming Musik:
#Paket Bronze: Biaya administrasi 1%, akses dasar ke lagu-lagu populer.
#Paket Silver: Biaya administrasi 3%, akses lagu premium dan playlist kustom.
#Paket Gold: Biaya administrasi 5%, akses lagu premium, playlist kustom, dan mode offline.
#Paket Platinum: Biaya administrasi 7%, akses semua fitur, playlist kustom, mode offline, dan konten eksklusif artis.
#3. Tampilan Hasil
#Untuk setiap paket, tampilkan total bayar (termasuk biaya administrasi) dan detail keuntungan dari paket yang dipilih.
#4. Rumus
#Total bayar = Biaya Langganan + (Biaya Langganan x Biaya Admin) 


Harga = 1500000
Nama_Pengguna = "Sufi Ridho Utomo"
NIM_Pengguna = "2509106101"

Nama = str(input("Nama Lengkap : "))
NIM = int(input("NIM : "))

if Nama == Nama_Pengguna and NIM == int(NIM_Pengguna):
    print("Login Berhasil!")
    print("==Selamat datang di aplikasi streaming musik!==")
    print("Pilih paket langganan Anda:")
    print("1. Paket Bronze (Biaya Admin 1%) - Akses dasar ke lagu-lagu populer")
    print("2. Paket Silver (Biaya Admin 3%) - Akses lagu premium dan playlist kustom")
    print("3. Paket Gold (Biaya Admin 5%) - Akses lagu premium, playlist kustom, dan mode offline")
    print("4. Paket Platinum (Biaya Admin 7%) - Akses semua fitur, playlist kustom, mode offline, dan konten eksklusif artis")
    print("[Harga Paket Sama = Rp.1.500.000]")
    
    pilihan = input("Masukkan pilihan paket (1-4): ")
    
    if pilihan == '1':
        admin = 0.01
        total_bayar = Harga + (Harga * admin)
        print(f"Total bayar untuk Paket Bronze: Rp {int(total_bayar)}")
        print("=> Benefit: Akses dasar ke lagu-lagu populer <=")
        print("==Terima Kasih Telah Berlangganan==")
    elif pilihan == '2':
        admin = 0.03
        total_bayar = Harga + (Harga * admin)
        print(f"Total bayar untuk Paket Silver: Rp {int(total_bayar)}")
        print("=> Benefit: Akses lagu premium dan playlist kustom <=")
        print("==Terima Kasih Telah Berlangganan==")
    elif pilihan == '3':
        admin = 0.05
        total_bayar = Harga + (Harga * admin)
        print(f"Total bayar untuk Paket Gold: Rp {int(total_bayar)}")
        print("=> Benefit: Akses lagu premium, playlist kustom, dan mode offline <=")
        print("==Terima Kasih Telah Berlangganan==")
    elif pilihan == '4':
        admin = 0.07
        total_bayar = Harga + (Harga * admin)
        print(f"Total bayar untuk Paket Platinum: Rp {int(total_bayar)}")
        print("=> Benefit: Akses semua fitur, playlist kustom, mode offline, dan konten eksklusif artis <=")
        print("==Terima Kasih Telah Berlangganan==")
    else:
        print("Pilihan tidak valid.")
else:
    print("Login Gagal! Silakan coba lagi.")
