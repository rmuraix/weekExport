import pyperclip
import datetime
import json
import sys
import os

def main():
    print("copyright (c) Ryota Murai")
    print("Repository: https://github.com/rmuraix/weekExport\n")

    is_file = os.path.isfile("./run_config.json")
    default_config = {"style": "EN", "start": 1, "loop": 1, "days": 7}

    if is_file:
        with open("./run_config.json") as f:
            config = json.load(f)

        # Check if JSON has the necessary keys.
        # If not, add the default values.
        for key, value in default_config.items():
            if key not in config:
                print(f"{key} is not found in config file. So use the default: {value}")
                config[key] = value

        # Verify that the key value is correct.
        # If not correct, end the program.
        is_correct = check_config(config)
        if not is_correct:
            print("Incorrect value in config file.")
            sys.exit(1)
    else:
        config = default_config
        with open("./run_config.json", "w") as f:
            json.dump(config, f, indent=4)

    today = datetime.date.today()
    monday = get_monday(today, config["start"])

    export_str = genarate_str(monday, config)

    # copy to clipboard
    pyperclip.copy(export_str)

    input("Copied to Clipboard! Press Enter to Exit.")


def check_config(config):
    if type(config["style"]) != str:
        return False
    if type(config["start"]) != int:
        return False
    if type(config["loop"]) != int:
        return False
    if type(config["days"]) != int:
        return False

    if config["style"] not in ["JP", "EN"]:
        print("Invalid style")
        return False
    if config["loop"] < 1:
        print("Invalid loop")
        return False
    if config["days"] < 1:
        print("Invalid days")
        return False
    return True


def get_monday(today, start):
    monday = today - datetime.timedelta(days=today.weekday()) + datetime.timedelta(days=start * 7)
    return monday


def genarate_str(monday, config):
    # japanese weekdays
    d_week = {
        "Sun": "日",
        "Mon": "月",
        "Tue": "火",
        "Wed": "水",
        "Thu": "木",
        "Fri": "金",
        "Sat": "土",
    }

    export_str = ""
    
    for i in range(config["loop"]):
        
        monday = monday + datetime.timedelta(days=config["start"] * (7 * i))
        for j in range(config["days"]):
            d = monday + datetime.timedelta(days=j)
            if config["style"] == "JP":
                key = d.strftime("%a")
                w = d_week[key]
                d = d.strftime("%m/%d") + f"({w})"
            else:
                d = d.strftime("%m/%d(%a)")
            export_str += str(d) + "\n"

    return export_str

if __name__ == "__main__":
    main()