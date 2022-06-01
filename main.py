import subprocess
import process
import pyperclip

def main():
    print('copyright (c) Ryota Murai')
    print('Repository: https://github.com/rmuraix/weekExport\n')

    exportStr = process.process()

    pyperclip.copy(exportStr)

    print('Copied to Clipboard! Exit the program after the next action.')
    subprocess.call('PAUSE', shell=True)

if __name__=="__main__":
    main()