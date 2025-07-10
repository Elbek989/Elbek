class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

class Task:
    def __init__(self, user_id, task, time, is_active=True):
        self.user_id = user_id
        self.task = task
        self.time = time
        self.is_active = is_active

users = [
    User(1, "ali", "1234"),
    User(2, "vali", "qwerty")
]
tasks = []

while True:
    print("\n1) Login")
    print("2) Chiqish")
    tanlov = input("Tanlang: ")

    if tanlov == '1':
        username = input("Username kiriting: ")
        password = input("Password kiriting: ")

        active_user = None
        for user in users:
            if user.username == username and user.password == password:
                active_user = user
                break

        if active_user:
            print("Tizimga kirdingiz:", active_user.username)
            while True:
                print("\n1) Tasklarni ko‘rish")
                print("2) Task qo‘shish")
                print("3) Taskni o‘chirish")
                print("4) Taskni yangilash")
                print("5) Chiqish")
                ichki_tanlov = input("Tanlang: ")

                if ichki_tanlov == '1':
                    print("\nSizning aktiv tasklaringiz:")
                    index = 1
                    for task in tasks:
                        if task.user_id == active_user.id and task.is_active:
                            print(f"{index}) {task.task} - {task.time}")
                            index += 1
                    if index == 1:
                        print("Tasklar mavjud emas.")

                elif ichki_tanlov == '2':
                    task_text = input("Task matnini kiriting: ")
                    task_time = input("Task vaqti (masalan, 14:00): ")
                    new_task = Task(active_user.id, task_text, task_time)
                    tasks.append(new_task)
                    print("Task qo‘shildi.")

                elif ichki_tanlov == '3':
                    print("\nO'chirmoqchi bo‘lgan taskni tanlang:")
                    visible_tasks = []
                    for task in tasks:
                        if task.user_id == active_user.id and task.is_active:
                            visible_tasks.append(task)
                    for i, task in enumerate(visible_tasks):
                        print(f"{i+1}) {task.task} - {task.time}")
                    if len(visible_tasks) == 0:
                        print("Tasklar mavjud emas.")
                        continue
                    delete_index = int(input("Raqamini kiriting: ")) - 1
                    if 0 <= delete_index < len(visible_tasks):
                        visible_tasks[delete_index].is_active = False
                        print("Task o‘chirildi.")
                    else:
                        print("Noto‘g‘ri raqam.")

                elif ichki_tanlov == '4':
                    print("\nO‘zgartirmoqchi bo‘lgan taskni tanlang:")
                    visible_tasks = []
                    for task in tasks:
                        if task.user_id == active_user.id and task.is_active:
                            visible_tasks.append(task)
                    for i, task in enumerate(visible_tasks):
                        print(f"{i+1}) {task.task} - {task.time}")
                    if len(visible_tasks) == 0:
                        print("Tasklar mavjud emas.")
                        continue
                    update_index = int(input("Raqamini kiriting: ")) - 1
                    if 0 <= update_index < len(visible_tasks):
                        new_text = input("Yangi task matni: ")
                        new_time = input("Yangi vaqt: ")
                        visible_tasks[update_index].task = new_text
                        visible_tasks[update_index].time = new_time
                        print("Task yangilandi.")
                    else:
                        print("Noto‘g‘ri raqam.")

                elif ichki_tanlov == '5':
                    print("Tizimdan chiqildi.")
                    break

                else:
                    print("Noto‘g‘ri tanlov.")

        else:
            print("Login yoki parol noto‘g‘ri.")

    elif tanlov == '2':
        print("Dasturdan chiqildi.")
        break

    else:
        print("Noto‘g‘ri tanlov.")
