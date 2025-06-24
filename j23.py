import json

from unicodedata import category


def add_object():
    with open("data.json","r")as file:
        data=json.load(file)
    count=0
    for item in data.keys():
        count+=1
        print(f"{count},",item)
    category=input("category tanlang=")
    countlen=str(len(data[category])+1)
    model=input("model:")
    price=input("price:")
    new_obj={
        "model":model,
        "price":price
    }
    data[category][f'{countlen}'] = new_obj
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)
def update_data(category:str,id:str,parametr:str,value):
    with open("data.json",'r') as file:
        data=json.load(file)
    data[category][id][parametr]=value
    with open('data.json','w') as file:
        json.dump(data,file,indent=4)
add_object()