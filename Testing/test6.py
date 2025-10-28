namaMahasiswa = ["Andre", "Anton", "Wawan", "Endang" ,"Eko" ]
IPK = ["1", "2", "3", "4"]
print("Daftar Mahasiswa")
print("No | Nama     | IPK")
for i in range(len(namaMahasiswa)):
    print(f"{i+1:2} | {namaMahasiswa[i]:8} | {IPK[i%len(IPK)]:3}")
print("Terima kasih telah melihat daftar mahasiswa!")