import pyperclip
import datetime
import json
import sys


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

    export_str = genarate_str(config)
    pyperclip.copy(export_str)  # copy to clipboard

    input("\nCopied to Clipboard! Press Enter to Exit.")


def genarate_json(
    json_path,
):  # generate json file When "./run_config.json" cannot be found
    json_str = {"style": "EN", "start": 1, "loop": 1, "days": 7}
    with open(json_path, "w") as f:
        json.dump(json_str, f, indent=4)


def genarate_str(config):
    try:
        style = config["style"]
    except KeyError:
        print("style is not found in config file. So use the default: EN")
        style = "EN"
    try:
        start = config["start"]
    except KeyError:
        print("start is not found in config file. So use the default: 1")
        start = 1
    try:
        loop = config["loop"]
    except KeyError:
        print("loop is not found in config file. So use the default: 1")
        loop = 1
    try:
        days = config["days"]
    except KeyError:
        print("days is not found in config file. So use the default: 7")
        days = 7

    export_str = ""

    # check rule
    if style not in ["JP", "EN"]:
        print("Invalid style")
        sys.exit()
    if (type(start) is int) is not True:
        print("start must be integer")
        sys.exit()
    if (type(loop) is int) is not True:
        print("loop must be integer")
        sys.exit()
    if loop < 1:
        print("loop must be greater than 0")
        sys.exit()
    if (type(days) is int) is not True:
        print("days must be integer")
        sys.exit()
    elif (days < 1) or (days > 7):
        print("days must be 1-7")
        sys.exit()

    now_date = datetime.date.today()
    monday = now_date - datetime.timedelta(days=now_date.weekday())
    monday = monday + datetime.timedelta(days=start * 7)  # start from monday

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

    if style == "JP":
        for i in range(loop):
            monday = monday + datetime.timedelta(days=start * (7 * i))
            for j in range(days):
                d = monday + datetime.timedelta(days=j)
                key = d.strftime("%a")
                w = d_week[key]
                d = d.strftime("%m/%d") + f"({w})"
                export_str += str(d) + "\n"
    elif style == "EN":
        for i in range(loop):
            monday = monday + datetime.timedelta(days=start * (7 * i))
            for j in range(days * loop):
                d = monday + datetime.timedelta(days=j)
                d = d.strftime("%m/%d(%a)")
                export_str += str(d) + "\n"

    return export_str


if __name__ == "__main__":
    main()
