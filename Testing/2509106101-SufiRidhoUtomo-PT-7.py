import os
os.system()

users = {
    'Admin': {'password': 'Sufi123', 'role': 'admin'},
    'Sufi': {'password': 'Sufi321', 'role': 'customer'}
}

products = {
    'tickets': [
        [1, "Event Ticket (Thur-Sun)", 1500000, 100],
        [2, "Weekend Ticket (Fri-Sun)", 1300000, 200],
        [3, "Race Ticket", 1150000, 300],
        [4, "Day Ticket", 700000, 350],
        [5, "Paddock Access Add-on", 1000000, 75]
    ],
    'merchandise': [
        [1, "N24H Official T-Shirt", 1200000, 100],
        [2, "N24H Cap", 600000, 120],
        [3, "N24H SunGlasses", 2700000, 75],
        [4, "Wall Clock (NBR)", 700000, 100],
        [5, "Scale Model Car 1:43", 1300000, 75]
    ]
}

activity = {
    'carts': {
        'Sufi': []
    },
    'transactions': []
}


def register():
    print("\n ==| User Registration |==")
    
    username = input("New Username: ")

    if username in users:
        print("\nUsername Already used!")
        return

    password = input("New Password: ")
    users[username] = {'password': password, 'role': 'customer'}
    activity['carts'][username] = [] 
    print(f"Registration Successful: {username}")

def login():
    print("\n ==| Login Admin/Customer |==")
    print("+————————————————————————————+")
    username = input("Username: ")
    password = input("Password: ")
    print(" ")

    user_data = users.get(username)
    
    if user_data and user_data['password'] == password:
        print(f"Login Successful, Welcome {username}!")
        return username, user_data['role']
    
    print("Invalid Username or Password!!")
    return None, None

def display_products(product_list, title):
    print(f"\n ==| {title} |==")
    print("+—————+——————————————————————————————+——————————————————+————————+")
    print("| ID  | Nama Produk                  | Harga            | Stok  |")
    print("+—————+——————————————————————————————+——————————————————+————————+")
    for item in product_list:
        print(f"| {item[0]:^3} | {item[1]:<28} | Rp {item[2]:>11,} | {item[3]:^5} |")
    print("+—————+——————————————————————————————+——————————————————+————————+")

def add_to_cart(username, product_type):
    product_list = products['tickets'] if product_type == 'tiket' else products['merchandise']
    title = "Daftar Tiket" if product_type == 'tiket' else "Daftar Merchandise"
    display_products(product_list, title)
    
    item_id_str = input("Enter The Product ID You Want To Buy: ")
    
    if not item_id_str.isdigit():
        print("Invalid ID Input, Must Be A Number.")
        return

    item_id = int(item_id_str)
    selected_item = None
    for item in product_list:
        if item[0] == item_id:
            selected_item = item
            break
            
    if not selected_item:
        print("ID Product Not Found.")
        return

    quantity_str = input(f"Amount '{selected_item[1]}' What You Want To Buy: ")
    
    if not quantity_str.isdigit() or int(quantity_str) <= 0:
        print("Invalid Number, Number Must Be A Greater Than 0.")
        return
        
    quantity = int(quantity_str)
    
    if quantity > selected_item[3]:
        print(f"Insufficient Stock. Remaining Stock: {selected_item[3]}")
        return

    activity['carts'][username].append({'item': selected_item, 'quantity': quantity, 'type': product_type})
    print(f"Successfully Added {quantity} x {selected_item[1]} To Cart.")

def view_cart(username):
    print("\n ==| Your Shopping Cart |==")
    user_cart = activity['carts'].get(username, [])

    if not user_cart:
        print("Your Cart Is Empty.")
        return

    print("+——————+——————————————————————————————+——————————+——————————————————+")
    print("| No.  | Nama Produk                  | Jumlah   | Subtotal         |")
    print("+——————+——————————————————————————————+——————————+——————————————————+")
    
    total_price = 0
    for i, cart_item in enumerate(user_cart, 1):
        item_details = cart_item['item']
        quantity = cart_item['quantity']
        subtotal = item_details[2] * quantity
        total_price += subtotal
        print(f"| {i:^4} | {item_details[1]:<28} | {quantity:^8} | Rp {subtotal:>11,} |")
    
    print("+——————+——————————————————————————————+——————————+——————————————————+")
    total_str = f"Rp {total_price:,}"
    print(f"| Total Pembayaran:{total_str: >52} |")
    print("+————————————————————————————————————————————————————————————————————+")


def checkout(username):
    user_cart = activity['carts'].get(username, [])
    
    if not user_cart:
        print("Your Cart Is Empty. There Is Nothing To Checkout.")
        return

    print("\n ==| Checkout Cart |==")
    print("+—————————————————————+")
    
    for cart_item in user_cart:
        item_id = cart_item['item'][0]
        product_list = products['tickets'] if cart_item['type'] == 'tiket' else products['merchandise']
        
        current_item_stock = -1
        for db_item in product_list:
            if db_item[0] == item_id:
                current_item_stock = db_item[3]
                break
        
        if cart_item['quantity'] > current_item_stock:
            print(f"Sorry, Stock For '{cart_item['item'][1]}' Has Run Out/Decreased. Transaction Cancelled.")
            return

    total_price = 0
    for cart_item in user_cart:
        item_details = cart_item['item']
        quantity = cart_item['quantity']
        item_details[3] -= quantity
        total_price += item_details[2] * quantity

    activity['transactions'].append({'customer': username, 'items': user_cart, 'total': total_price})
    activity['carts'][username] = []
    print(f"Transaction Successful, Total Payment: Rp{total_price}. Thanks!")

def admin_view_transactions():
    print("\n ==| Report Of All Transactions |==")
    print("+——————————————————————————————————+")
    
    if not activity['transactions']:
        print("None Transaction.")
        return
        
    for i, trans in enumerate(activity['transactions'], 1):
        print(f"Transaction #{i}")
        print(f"  Customer: {trans['customer']}")
        print(f"  Total    : Rp{trans['total']:,}")
        print("  Detail Item:")
        for cart_item in trans['items']:
            item = cart_item['item']
            quantity = cart_item['quantity']
            print(f"    - {item[1]} (x{quantity})")
        print("-" * 30)

def admin_select_product():
    choice = input("Select Product Category (1: Ticket, 2: Merchandise): ")
    if choice == '1':
        product_list = products['tickets']
        display_products(product_list, "Ticket List")
    elif choice == '2':
        product_list = products['merchandise']
        display_products(product_list, "Merchandise List")
    else:
        print("Invalid Category.")
        return None

    item_id_str = input("Enter The Product To Be Set: ")
    if not item_id_str.isdigit():
        print("Invalid ID Input, Must Be A Number.")
        return None

    item_id = int(item_id_str)
    for item in product_list:
        if item[0] == item_id:
            return item 
    
    print("Product Not Found.")
    return None

def admin_update_price():
    print("\n ==| Change Price |==")
    print("+————————————————————+")
    item_to_manage = admin_select_product()
    
    if not item_to_manage:
        return 
        
    print(f"Change The Price For: '{item_to_manage[1]}'")
    print(f"Current Price: Rp{item_to_manage[2]}")
    
    new_price_str = input("Enter New Price: ")
    if not new_price_str.isdigit() or int(new_price_str) < 0:
        print("Invalid Price, Must Be A Non-Negative Number.")
        return
        
    item_to_manage[2] = int(new_price_str)
    print("Price Changed Successfully")

def admin_add_stock():
    print("\n ==| Add Product Stock |==")
    print("+—————————————————————————+")
    item_to_manage = admin_select_product()

    if not item_to_manage:
        return
        
    print(f"Add Stock To: '{item_to_manage[1]}'")
    print(f"Currrent Stock: {item_to_manage[3]}")
    
    amount_str = input("Stock Quantity Increased: ")
    if not amount_str.isdigit() or int(amount_str) <= 0:
        print("Invalid Number, Must Be A Positive Number.")
        return
        
    item_to_manage[3] += int(amount_str)
    print(f"Stock Added Successfully. New Stock: {item_to_manage[3]}")

def admin_set_stock():
    print("\n ==| Product Stock Reset |==")
    print("+———————————————————————————+")
    item_to_manage = admin_select_product()

    if not item_to_manage:
        return
        
    print(f"Reset Stock For: '{item_to_manage[1]}'")
    print(f"Current Stock: {item_to_manage[3]}")
    
    new_stock_str = input("Enter New Stock Quantity: ")
    if not new_stock_str.isdigit() or int(new_stock_str) < 0:
        print("Invalid Number, Must Be A Non-Negative Number.")
        return
        
    item_to_manage[3] = int(new_stock_str)
    print(f"Stock Successfully Reset, New Stock: {item_to_manage[3]}")

def customer_menu(username):
    print("\n ==| Customer Menu |==")
    print("+—————————————————————+")
    print("| 1. Beli Tiket       |")
    print("| 2. Beli Merchandise |")
    print("| 3. Lihat Keranjang  |")
    print("| 4. Checkout         |")
    print("| 5. Logout           |")
    print("+—————————————————————+")
    choice = input("Enter Your Choice: ")

    if choice == '1':
        add_to_cart(username, 'tiket')
        customer_menu(username)
    elif choice == '2':
        add_to_cart(username, 'merch')
        customer_menu(username)
    elif choice == '3':
        view_cart(username)
        customer_menu(username)
    elif choice == '4':
        checkout(username)
        customer_menu(username)
    elif choice == '5':
        print("You Have Logged Out.")
        return
    else:
        print("Invalid Choice.")
        customer_menu(username)

def admin_menu():
    print("\n ==| Admin Menu |==")
    print("+————————————————————————————+")
    print("| 1. Laporan Transaksi       |")
    print("| 2. Ubah Harga Produk       |")
    print("| 3. Tambah Stok Produk      |")
    print("| 4. Atur Ulang Stok Produk  |")
    print("| 5. Logout                  |")
    print("+————————————————————————————+")
    choice = input("Enter Your Choice: ")

    if choice == '1':
        admin_view_transactions()
        admin_menu()
    elif choice == '2':
        admin_update_price()
        admin_menu()
    elif choice == '3':
        admin_add_stock()
        admin_menu()
    elif choice == '4':
        admin_set_stock()
        admin_menu()
    elif choice == '5':
        print("You Have Logged Out.")
        return
    else:
        print("Invalid Choice.")
        admin_menu()

def main_menu():
    print("\n ==| Welcome To Nürburgring |==")
    print("+——————————————————————————————+")
    print("|       1. Registration        |")
    print("|          2. Login            |")
    print("|          3. Exit             |")
    print("+——————————————————————————————+")
    choice = input("Enter Your Choice: ")

    if choice == '1':
        register()
        main_menu()
    elif choice == '2':
        username, role = login()
        if username and role == 'customer':
            customer_menu(username)
        elif username and role == 'admin':
            admin_menu()
        main_menu()
    elif choice == '3':
        print("Thanks For Using Nürburgring")
        return
    else:
        print("Invalid Choice!!, Try Again")
        main_menu()

if __name__ == "__main__":
    main_menu()