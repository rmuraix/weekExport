import pyperclip
import datetime


def main():
    print("copyright (c) Ryota Murai")
    print("Repository: https://github.com/rmuraix/weekExport\n")

    exportStr = exWeek()

    pyperclip.copy(exportStr)

    input("Copied to Clipboard! Press Enter to Exit.")


def exWeek():

    dtNow = datetime.date.today()
    weekday = dtNow.weekday()

    result = ""

    d_week = {
        "Sun": "日",
        "Mon": "月",
        "Tue": "火",
        "Wed": "水",
        "Thu": "木",
        "Fri": "金",
        "Sat": "土",
    }

    for i in range(7):
        daysDelta = 7 - weekday + i

        d = dtNow + datetime.timedelta(days=daysDelta)

        key = d.strftime("%a")
        w = d_week[key]

        formatDate = d.strftime("%m/%d") + f"({w})"

        result += str(formatDate) + "\n"

    return result


if __name__ == "__main__":
    main()
