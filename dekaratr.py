def febanci(n:int):
    if n==1:
        return 1
    elif n==2:
        return 1
    return febanci(n-2)+febanci(n-1)
print(febanci(4))