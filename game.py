#game

import random
import time
import tkinter as tk
from tkinter import ttk
from tkinter import *
import os


gui = tk.Tk()
gui.geometry('700x400')
gui.resizable(False,False)
gui.title("HANGMAN")
gui.iconbitmap('IMAGES/download.ico')

with open("player_name.txt", "r") as file:
    name = file.read()


    

lblDisplay1 = Label(gui, text=f"Welcome to Hangman, {name}!", font=("courier", 20, "bold"))
lblDisplay1.pack(ipadx=0, ipady=60)
difficulty = Label(gui, text="please choose your desired difficulty for this game")




gui.mainloop()