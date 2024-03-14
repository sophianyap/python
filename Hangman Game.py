#Hangman Game

import tkinter as tk
from tkinter import ttk
from tkinter import *
namelist = []

#guiwindow
gui = tk.Tk()
gui.geometry('550x340')
gui.resizable(False,False)
gui.title("HANGMAN")
gui.iconbitmap('IMAGES/download.ico')

lblDisplay1= Label(gui,text="Hangman", font=("courier", 20,"bold"))
lblDisplay1.pack(ipadx=0,ipady=60,)
lblDisplay2 = Label(gui, text="please enter your name", font=('courier',8))
lblDisplay2.pack()

def gotogame():
     if name in namelist:
        gui.destroy()
        import game
          

def addname():
    if name == " ":
        lblDisplay1 = Label(text= "please enter your name",font="courier")
        lblDisplay1.pack(ipadx=2,ipady=1)

    
    else:
        if txtName not in namelist:
            namelist.append(name)
            
            if name in namelist:
                lblDisplay= Label(text="Player name saved!")
                instruction= Label(text="welcome to hangman",font="courier")
                instruction.pack(ipadx=2, ipady=1)
                startbtn = ttk.Button(gui, text = "go to game", command=gotogame)
                startbtn.pack(ipadx=7, ipady=1)
                
          
txtName = ttk.Entry(font="courier")
txtName.pack(ipadx=2)
name = str(txtName.get().strip())
txtName.focus()
Entername = ttk.Button(gui, text = "enter",command=addname)
Entername.pack(ipadx=5, ipady=1)


gui.mainloop()




    
        
        



    
