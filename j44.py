import json

def json_manager(f_name: str, status: str, data=None):
    if status == "r":
        with open(f'{f_name}', f'{status}') as f:
            data_json = json.load(f)
            return data_json
    elif status == "w":
        with open(f'{f_name}', f'{status}') as f:
            json.dump(data, f, indent=4)
            return "add"
    else:
        try:
            with open(f'{f_name}', "r") as f:
                data_json = json.load(f)
            data_json.update(data)
            with open(f'{f_name}', "w") as f:
                json.dump(data_json, f, indent=4)
            return "add"
        except Exception as e:
            with open(f'{f_name}', "w") as f:
                json.dump(data, f, indent=4)
            return "add"

# Foydalanuvchidan input olish
o = int(input(
    "Ma'lumotlarni ko'rish uchun 1 ni bosing\n"
    "User qo'shish uchun 2 ni bosing\n"
    "Chiqib ketish uchun 3 ni bosing\n"
))

if o == 1:
    data = json_manager("data.json", "r")
    print(data)

elif o == 2:
    ism = input("Ismingizni kiriting: ")
    yosh = input("Yoshingizni kiriting: ")
    yangi_user = {ism: yosh}
    json_manager("data.json", "else", yangi_user)

elif o == 3:
    print("Dasturdan chiqildi.")
else:
    print("Noto'g'ri son kiritildi.")