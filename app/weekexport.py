import pyperclip
import datetime
import json

def main():
    print("copyright (c) Ryota Murai")
    print("Repository: https://github.com/rmuraix/weekExport\n")

    json_path = "./run_config.json"
    try:
        with open(json_path) as f:
            config = json.load(f)
    except FileNotFoundError:
        genarate_json(json_path)
        with open(json_path) as f:
            config = json.load(f)
    
    print(config['style'])
    print(config['start'])
    print(config['loop'])

def genarate_json(json_path): # generate json file When "./run_config.json" cannot be found
    str = {
    "style": "JP",
    "start": 1,
    "loop": 1    
    }
    with open(json_path, 'w') as f:
        json.dump(str, f, indent=4)

if __name__ == "__main__":
    main()
