Nama_Pengguna = "Budi"
NIM_Pengguna = 12345

percobaan = 3  # maksimal 3 kali percobaan

while percobaan > 0:
    Nama = input("Nama Lengkap : ")
    NIM = int(input("NIM : "))

    if Nama == Nama_Pengguna and NIM == NIM_Pengguna:
        print("Login Berhasil! Selamat datang,", Nama)
        break
    else:
        percobaan -= 1
        if percobaan > 0:
            print("Login Gagal! Silahkan ulangi kembali.")
            print("Sisa percobaan:", percobaan)
        else:
            print("Login Anda Mencapai Limit!")
