with open("file.txt", "r") as f:
    s = f.readlines()


a = [int(item) for line in s for item in line.split()]
l=-1
g = []

