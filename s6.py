b=str(input("belgi kiriting"))
if ord(b)>47 and ord(b)<58:
    print("digit")
elif ord(b)>64 and ord(b)<91 or ord(b)>96 and ord(b)<123:
    print("lotin alifbosi")
else:
    print(0)
