import json

def json_manager(f_name: str, status: str, data=None):
    if status == "r":
        with open(f'{f_name}', f'{status}') as f:
            data_json = json.load(f)
            return data_json
    elif status == "w":
        with open(f'{f_name}', f'{status}') as f:
            json.dump(data, f, indent=4)
            return "add "
    else:
        try:
            with open(f'{f_name}', "r") as f:
                data_json = json.load(f)
            data_json.update(data)
            with open(f'{f_name}', "w") as f:
                json.dump(data_json, f, indent=4)
            return "add "
        except Exception as e:
            with open(f"{f_name}","w")as f:
                json.dump(data,f,indent=4)
                return "add"





