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
    pyperclip.copy(export_str)

    input("Copied to Clipboard! Press Enter to Exit.")


def genarate_json(
    json_path,
):  # generate json file When "./run_config.json" cannot be found
    json_str = {"style": "JP", "start": 1, "loop": 1, "days": 7}
    with open(json_path, "w") as f:
        json.dump(json_str, f, indent=4)


def genarate_str(config):
    style = config["style"]
    start = config["start"]
    loop = config["loop"]
    days = config["days"]
    export_str = ""

    # rule　check
    if style not in ["JP", "EN"]:
        print("Invalid style")
        sys.exit()
    if (type(start) is int) == False:
        print("start must be integer")
        sys.exit()
    if (type(loop) is int) == False:
        print("loop must be integer")
        sys.exit()
    if loop < 1:
        print("loop must be greater than 0")
        sys.exit()
    if (days < 1) or (days > 7):
        print("days must be 1-7")
        sys.exit()

    now_date = datetime.date.today()
    monday = now_date - datetime.timedelta(days=now_date.weekday())

    d_week = {
        "Sun": "日",
        "Mon": "月",
        "Tue": "火",
        "Wed": "水",
        "Thu": "木",
        "Fri": "金",
        "Sat": "土",
    }

    monday = monday + datetime.timedelta(days=start * 7)

    if style == "JP":
        for j in range(days * loop):
            d = monday + datetime.timedelta(days=j)
            key = d.strftime("%a")
            w = d_week[key]
            d = d.strftime("%m/%d") + f"({w})"
            export_str += str(d) + "\n"
    elif style == "EN":
        for j in range(days * loop):
            d = monday + datetime.timedelta(days=j)
            d = d.strftime("%m/%d(%a)")
            export_str += str(d) + "\n"

    return export_str


if __name__ == "__main__":
    main()
