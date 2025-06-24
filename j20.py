import json



def load_data(filename='data.json'):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
def view_products(data):
    if not data:
        print("Hozirda mahsulotlar mavjud emas.")
    else:
        for index, product in enumerate(data, 1):
            print(f"{index}. {product['name']} - {product['price']} so'm")


def add_product(data, filename='data.json'):
    name = input("Mahsulot nomini kiriting: ")
    price = input("Mahsulot narxini kiriting: ")
    product = {'name': name, 'price': price}
    data.append(product)


    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
    print(f"{name} mahsuloti muvaffaqiyatli qo'shildi!")


# Mahsulotni tahrirlash
def edit_product(data, filename='data.json'):
    try:
        index = int(input("Tahrir qilmoqchi bo'lgan mahsulotingiz raqamini kiriting: ")) - 1
        if 0 <= index < len(data):
            new_name = input("Yangi nomni kiriting: ")
            new_price = input("Yangi narxni kiriting: ")
            data[index]['name'] = new_name
            data[index]['price'] = new_price

            # JSON faylga yangilangan ma'lumotni yozish
            with open(filename, 'w') as file:
                json.dump(data, file, indent=4)
            print("Mahsulot muvaffaqiyatli tahrirlandi!")
        else:
            print("Noto'g'ri raqam kiritildi.")
    except ValueError:
        print("Iltimos, to'g'ri raqam kiriting.")


# Tizimdan chiqish
def exit_system():
    print("Dasturdan chiqilmoqda... Yaxshi kun!")
    exit()



def main():
    filename = 'data.json'
    data = load_data(filename)

    while True:
        print("\n--- Mahsulotlar Boshqaruvi ---")
        print("1. Mahsulotlarni ko'rish")
        print("2. Yangi mahsulot qo'shish")
        print("3. Mahsulotni tahrirlash")
        print("4. Tizimdan chiqish")

        choice = input("Tanlovingizni kiriting (1-4): ")

        if choice == '1':
            view_products(data)
        elif choice == '2':
            add_product(data, filename)
        elif choice == '3':
            edit_product(data, filename)
        elif choice == '4':
            exit_system()
        else:
            print("Noto'g'ri tanlov! Iltimos, 1-4 orasida tanlov qiling.")


