namaMahasiswa = ["Andre", "Jaki", "Wawan", "Endang" ,"Gandi" ]
NIM = [121, 174, 113, 94, 132]
namaMahasiswa.sort()
print(namaMahasiswa)
NIM.sort()
print(NIM)
print("Daftar Mahasiswa")
print("No | Nama     | NIM")
for i in range(len(namaMahasiswa)):
    print(f"{i+1:2} | {namaMahasiswa[i]:8} | {NIM[i%len(NIM)]:3}")
print("Terima kasih telah melihat daftar mahasiswa!")

# buatlah sebuah tuple lakukan 1 menggabungkan 2 tuple, mengurutkan tuple, dan menghitung jumlah elemennt

barang = ("semen", "batu bata", "pasir", "besi")