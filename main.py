import subprocess
import process
import pyperclip

exportStr = process.process()

pyperclip.copy(exportStr)

print('Copied to Clipboard! Exit the program after the next action.')
subprocess.call('PAUSE', shell=True)