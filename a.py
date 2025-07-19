from contextlib import contextmanager
# @contextmanager
# def my_context():
#     print("Context ichiga kirdik")
#     try:
#         yield
#     finally:
#         print("Contextdan chiqyapmiz")
# with my_context():
#     print("============")
@contextmanager
def file_mngr(file_name,mode):
    f=None
    try:
        if "." not in file_name:
            raise NameError
        print(f"Fayl '{file_name}' ochilyati...")
        f=open(file_name,mode)
        yield f
    finally:
        if f:
            print(f"Fayl '{file_name}' yopilyati...")
            f.close()
with file_mngr('databases.py',"r") as file:
    f=file.read()
    print(f)