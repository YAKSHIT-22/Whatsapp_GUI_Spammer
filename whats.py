import time
import tkinter as tk
from tkinter import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

import os

def clear():
    name = os.name
    if name == 'nt':
        _ = os.system('cls')
    else:
        os.system('clear')


clear()
x="""\33[32m\n

 ┏┓┏┓┏┓┏┓━━━━━━━━┏┓━━━━━━━━━━━━━━━━━━━━━━┏━━━┓┏┓━┏┓┏━━┓━━━━┏━━━┓━━━━━━━━━━━━━━━━━━━━━━━━
 ┃┃┃┃┃┃┃┃━━━━━━━┏┛┗┓━━━━━━━━━━━━━━━━━━━━━┃┏━┓┃┃┃━┃┃┗┫┣┛━━━━┃┏━┓┃━━━━━━━━━━━━━━━━━━━━━━━━
 ┃┃┃┃┃┃┃┗━┓┏━━┓━┗┓┏┛┏━━┓┏━━┓━┏━━┓┏━━┓━━━━┃┃━┗┛┃┃━┃┃━┃┃━━━━━┃┗━━┓┏━━┓┏━━┓━┏┓┏┓┏┓┏┓┏━━┓┏━┓
 ┃┗┛┗┛┃┃┏┓┃┗━┓┃━━┃┃━┃━━┫┗━┓┃━┃┏┓┃┃┏┓┃━━━━┃┃┏━┓┃┃━┃┃━┃┃━━━━━┗━━┓┃┃┏┓┃┗━┓┃━┃┗┛┃┃┗┛┃┃┏┓┃┃┏┛
 ┗┓┏┓┏┛┃┃┃┃┃┗┛┗┓━┃┗┓┣━━┃┃┗┛┗┓┃┗┛┃┃┗┛┃━━━━┃┗┻━┃┃┗━┛┃┏┫┣┓━━━━┃┗━┛┃┃┗┛┃┃┗┛┗┓┃┃┃┃┃┃┃┃┃┃━┫┃┃━
 ━┗┛┗┛━┗┛┗┛┗━━━┛━┗━┛┗━━┛┗━━━┛┃┏━┛┃┏━┛━━━━┗━━━┛┗━━━┛┗━━┛━━━━┗━━━┛┃┏━┛┗━━━┛┗┻┻┛┗┻┻┛┗━━┛┗┛━
 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━┃┃━━┃┃━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┃┃━━━━━━━━━━━━━━━━━━━━━━
 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━┗┛━━┗┛━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┗┛━━━━━━━━━━━━━━━━━━━━━━

                                                                                                                                  
"""
y = 0
while y <= len(x):
    os.system('clear')
    os.system('cls')
    print(x[:y])
    time.sleep(0)
    y = y+1
def startBombing():
    victim=str(name.get())
    msg=str(message.get())
    num=msgCount.get()
    options=webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    PATH=Service('C:/Users/yaksh/Downloads/chromedriver.exe')
    driver=webdriver.Chrome(service=PATH,options=options)
    driver.get("https://web.whatsapp.com/")

    time.sleep(50)
    user=driver.find_element(by=By.XPATH, value='//span[@title = "{}"]'.format(victim))
    user.click()

    msg_box=driver.find_element(by=By.XPATH, value='//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div')
    for i in range(num):
        msg_box.send_keys(msg)
        time.sleep(1)
        msg_box.send_keys(Keys.RETURN)
    print("Work Done")

#GUI
root=tk.Tk()
root.title("Whatsapp Bombing")
root.geometry("500x500")
root.resizable(height=False,width=False)

headingLabel=Label(root,text="Wait for 15 - 30 sec to start BOOM!",font=('Helvetics',12,'bold'))
headingLabel.place(relx=.5,y=15,anchor='center')

# victim name label
Label(root,text="Enter Name/No.").place(x=120,y=80)
name=StringVar()
nameBox=Entry(root,textvariable=name).place(x=220,y=80)
#  Msg label
Label(root,text="Enter Message").place(x=120,y=150)
message=StringVar()
msgBox=Entry(root,textvariable=message).place(x=220,y=150)

Label(root,text="No Of Message").place(x=120,y=220)
msgCount=IntVar()
countBox=Entry(root,textvariable=msgCount).place(x=220,y=220)
tk.Button(root,text="Start Bombing",command=startBombing).place(relx=.5,y=300,anchor="center")
root.mainloop()
