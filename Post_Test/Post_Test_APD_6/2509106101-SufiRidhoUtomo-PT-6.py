import os
os.system("cls")

data = {
    "users": {
        "Admin": {"password": "Sufi123", "role": "admin"},
        "Customer": {"password": "Sufi456", "role": "customer"},
    },
    "carts": {"Sufi": []},
    "tickets": {
        1: {"name": "Event Ticket (Thur-Sun)", "price": 1500000, "stock": 100},
        2: {"name": "Weekend Ticket (Fri-Sun)", "price": 1300000, "stock": 200},
        3: {"name": "Race Ticket", "price": 1150000, "stock": 300},
        4: {"name": "Day Ticket", "price": 700000, "stock": 350},
        5: {"name": "Paddock Access Add-on", "price": 1000000, "stock": 75},
    },
    "merch": {
        1: {"name": "N24H Official T-Shirt", "price": 1200000, "stock": 100},
        2: {"name": "N24H Cap", "price": 600000, "stock": 120},
        3: {"name": "N24H Sunglasses", "price": 2700000, "stock": 75},
        4: {"name": "Wall Clock (NBR)", "price": 700000, "stock": 100},
        5: {"name": "Scale Model Car 1:43", "price": 1300000, "stock": 75},
    },
    "transactions": [],
    "state": {
        "pengguna_saat_ini": "",
        "peran_saat_ini": "",
        "hasil_input_int": None,
        "produk_dipilih": None,
        "jenis_produk": None,
        "admin_produk_dipilih": None,
        "admin_id_dipilih": None,
        "admin_jenis_dipilih": None,
    },
}

while True:
    print()
    print(" ==| Selamat Datang Di Nürburgring |==")
    print("+-------------------------------------+")
    print("1. Daftar")
    print("2. Login")
    print("3. Keluar")
    choice = input("pilih: ").strip()
    if choice == "1":
        print()
        print("== daftar akun ==")
        while True:
            username = input("username baru: ").strip()
            if username == "":
                print("username kosong.")
                break
            if username in data["users"]:
                print("username sudah ada, coba yang lain.")
                break
            password = input("password baru: ").strip()
            if password == "":
                print("password kosong.")
                break
            data["users"][username] = {"password": password, "role": "customer"}
            data["carts"][username] = []
            print("daftar sukses. silakan login sebagai:", username)
            break
        input("tekan enter... ")
    elif choice == "2":
        print()
        print("== login ==")
        username = input("username: ").strip()
        password = input("password: ").strip()
        user = data["users"].get(username)
        if user and user["password"] == password:
            data["state"]["pengguna_saat_ini"] = username
            data["state"]["peran_saat_ini"] = user["role"]
            print("login sukses. halo,", username)
        else:
            data["state"]["pengguna_saat_ini"] = ""
            data["state"]["peran_saat_ini"] = ""
            print("username atau password salah.")
        input("tekan enter... ")

        user = data["state"]["pengguna_saat_ini"]
        role = data["state"]["peran_saat_ini"]
        if user and role == "customer":
            while True:
                print()
                print("== menu pelanggan ==")
                print("1. beli tiket")
                print("2. beli merchandise")
                print("3. lihat keranjang")
                print("4. checkout")
                print("5. logout")
                ch = input("pilih: ").strip()
                if ch == "1" or ch == "2":
                    category = "tiket" if ch == "1" else "merch"
                    products = data["tickets"] if category == "tiket" else data["merch"]
                    title = "daftar tiket" if category == "tiket" else "daftar merchandise"

                    print()
                    print("== " + title + " ==")
                    print("{:<3} {:<30} {:>12} {:>8}".format("ID", "Nama", "Harga (Rp)", "Stok"))
                    print("-" * 60)
                    for ID_Barang in sorted(products.keys()):
                        p = products[ID_Barang]
                        print("{:<3} {:<30} {:>12,} {:>8}".format(ID_Barang, p["name"], p["price"], p["stock"]))
                    print("-" * 60)

                    s = input("masukkan id produk (kosong = batal): ").strip()
                    ID_Barang = None
                    if s != "":
                        ss = s
                        if (ss[0] in "+-" and ss[1:].isdigit()) or ss.isdigit():
                            try_int = ss
                            if try_int[0] == "+":
                                try_int = try_int[1:]
                            ID_Barang = int(try_int)
                        else:
                            ID_Barang = None
                    if ID_Barang is None or ID_Barang not in products:
                        print("id tidak valid atau batal.")
                    else:
                        s2 = input(f"jumlah untuk '{products[ID_Barang]['name']}' (kosong = batal): ").strip()
                        Jumlah = None
                        if s2 != "":
                            ss2 = s2
                            if (ss2[0] in "+-" and ss2[1:].isdigit()) or ss2.isdigit():
                                if ss2[0] == "+":
                                    ss2 = ss2[1:]
                                Jumlah = int(ss2)
                                if Jumlah <= 0:
                                    Jumlah = None
                            else:
                                Jumlah = None
                        if Jumlah is None:
                            print("jumlah tidak valid atau batal.")
                        elif Jumlah > products[ID_Barang]["stock"]:
                            print("stok tidak cukup. sisa:", products[ID_Barang]["stock"])
                        else:
                            data["carts"].setdefault(user, []).append({"id": ID_Barang, "quantity": Jumlah, "type": category})
                            print(f"berhasil tambah {Jumlah} x {products[ID_Barang]['name']} ke keranjang.")
                    input("tekan enter... ")

                elif ch == "3":
                    print()
                    print("== keranjang ==")
                    cart = data["carts"].get(user, [])
                    if not cart:
                        print("keranjang kosong.")
                    else:
                        total = 0
                        print("{:<3} {:<30} {:>6} {:>14}".format("No", "Nama", "Jumlah", "Subtotal"))
                        print("-" * 60)
                        for i, item in enumerate(cart, 1):
                            products = data["tickets"] if item["type"] == "tiket" else data["merch"]
                            p = products[item["id"]]
                            subtotal = p["price"] * item["quantity"]
                            total += subtotal
                            print("{:<3} {:<30} {:>6} {:>14,}".format(i, p["name"], item["quantity"], subtotal))
                        print("-" * 60)
                        print("total: rp", f"{total:,}", sep="")
                    input("tekan enter... ")

                elif ch == "4":
                    cart = data["carts"].get(user, [])
                    if not cart:
                        print("keranjang kosong.")
                    else:
                        stok_ok = True
                        for item in cart:
                            products = data["tickets"] if item["type"] == "tiket" else data["merch"]
                            if item["quantity"] > products[item["id"]]["stock"]:
                                print("stok tidak cukup untuk", products[item["id"]]["name"], ". transaksi dibatalkan.")
                                stok_ok = False
                                break
                        if not stok_ok:
                            print("cek lagi stok sebelum coba checkout.")
                        else:
                            total = 0
                            for item in cart:
                                products = data["tickets"] if item["type"] == "tiket" else data["merch"]
                                products[item["id"]]["stock"] -= item["quantity"]
                                total += products[item["id"]]["price"] * item["quantity"]
                            data["transactions"].append({"customer": user, "items": list(cart), "total": total})
                            data["carts"][user] = []
                            print("transaksi berhasil. total: rp", f"{total:,}", ". terima kasih!", sep="")
                    input("tekan enter... ")

                elif ch == "5":
                    print("logout.")
                    break
                else:
                    print("pilihan salah.")
                    input("tekan enter... ")

        elif user and role == "admin":
            while True:
                print()
                print("== menu admin ==")
                print("1. laporan")
                print("2. ubah harga")
                print("3. tambah stok")
                print("4. set stok")
                print("5. logout")
                ch = input("pilih: ").strip()
                if ch == "1":
                    print()
                    print("== laporan transaksi ==")
                    if not data["transactions"]:
                        print("belum ada transaksi.")
                    else:
                        for i, t in enumerate(data["transactions"], 1):
                            print(f"transaksi #{i} — pelanggan: {t['customer']}, total: rp{t['total']:,}")
                            for it in t["items"]:
                                products = data["tickets"] if it["type"] == "tiket" else data["merch"]
                                print(f"  - {products[it['id']]['name']} (x{it['quantity']})")
                            print("-" * 40)
                    input("tekan enter... ")

                elif ch in ("2", "3", "4"):
                    print("pilih: 1) tiket  2) merchandise")
                    cat_choice = input("pilih 1 atau 2: ").strip()
                    if cat_choice == "1":
                        products = data["tickets"]
                        ptype = "tiket"
                    elif cat_choice == "2":
                        products = data["merch"]
                        ptype = "merch"
                    else:
                        products = None
                        ptype = None
                        print("pilihan tidak valid.")
                    if not products:
                        print("batal.")
                        input("tekan enter... ")
                        continue

                    print()
                    print("== daftar produk ==")
                    print("{:<3} {:<30} {:>12} {:>8}".format("ID", "Nama", "Harga (Rp)", "Stok"))
                    print("-" * 60)
                    for ID_Barang in sorted(products.keys()):
                        p = products[ID_Barang]
                        print("{:<3} {:<30} {:>12,} {:>8}".format(ID_Barang, p["name"], p["price"], p["stock"]))
                    print("-" * 60)

                    s = input("masukkan id produk (kosong = batal): ").strip()
                    ID_Barang = None
                    if s != "":
                        ss = s
                        if (ss[0] in "+-" and ss[1:].isdigit()) or ss.isdigit():
                            if ss[0] == "+":
                                ss = ss[1:]
                            ID_Barang = int(ss)
                        else:
                            ID_Barang = None
                    if ID_Barang is None or ID_Barang not in products:
                        print("produk tidak ditemukan atau batal.")
                        input("tekan enter... ")
                        continue

                    if ch == "2":
                        print("produk:", products[ID_Barang]["name"], "harga sekarang: rp", f"{products[ID_Barang]['price']:,}", sep=" ")
                        s2 = input("harga baru (boleh 0): ").strip()
                        new_price = None
                        if s2 != "":
                            ss2 = s2
                            if (ss2[0] in "+-" and ss2[1:].isdigit()) or ss2.isdigit():
                                if ss2[0] == "+":
                                    ss2 = ss2[1:]
                                new_price = int(ss2)
                                if new_price < 0:
                                    new_price = None
                            else:
                                new_price = None
                        if new_price is None:
                            print("input tidak valid atau batal.")
                        else:
                            products[ID_Barang]["price"] = new_price
                            print("harga diubah.")
                        input("tekan enter... ")

                    elif ch == "3":
                        print("produk:", products[ID_Barang]["name"], "stok sekarang:", products[ID_Barang]["stock"])
                        s2 = input("jumlah tambah: ").strip()
                        add = None
                        if s2 != "":
                            ss2 = s2
                            if (ss2[0] in "+-" and ss2[1:].isdigit()) or ss2.isdigit():
                                if ss2[0] == "+":
                                    ss2 = ss2[1:]
                                add = int(ss2)
                                if add <= 0:
                                    add = None
                            else:
                                add = None
                        if add is None:
                            print("input tidak valid atau batal.")
                        else:
                            products[ID_Barang]["stock"] += add
                            print("stok ditambah. baru:", products[ID_Barang]["stock"])
                        input("tekan enter... ")

                    elif ch == "4":
                        print("produk:", products[ID_Barang]["name"], "stok sekarang:", products[ID_Barang]["stock"])
                        s2 = input("stok baru (>=0): ").strip()
                        new_stock = None
                        if s2 != "":
                            ss2 = s2
                            if (ss2[0] in "+-" and ss2[1:].isdigit()) or ss2.isdigit():
                                if ss2[0] == "+":
                                    ss2 = ss2[1:]
                                new_stock = int(ss2)
                                if new_stock < 0:
                                    new_stock = None
                            else:
                                new_stock = None
                        if new_stock is None:
                            print("input tidak valid atau batal.")
                        else:
                            products[ID_Barang]["stock"] = new_stock
                            print("stok di-set. sekarang:", products[ID_Barang]["stock"])
                        input("tekan enter... ")

                elif ch == "5":
                    print("logout.")
                    break
                else:
                    print("pilihan salah.")
                    input("tekan enter... ")

    elif choice == "3":
        print("terima kasih. sampai jumpa.")
        break
    else:
        print("pilihan salah.")
        input("tekan enter... ")
