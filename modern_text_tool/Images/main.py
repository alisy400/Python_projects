from tkinter import *
from tkinter import ttk
from tkinter import messagebox, filedialog
from tkinter.ttk import Combobox
import tkinter as tk

import pyttsx3
import PyPDF2
import os

import googletrans
from googletrans import Translator

import datetime
from gtts import gTTS
from playsound import playsound
import threading


framebg="#1e1e1e"
bodybg="#2c2c2c"
root = Tk()
root.title("Text tool")
root.geometry("1000x800")
root.resizable(False, False)
root.config(bg=bodybg)

#icon
image_icon=PhotoImage(file="icon.png")
root.iconphoto(False,image_icon)

#Top frame
Top_frame = Frame(root,bg=framebg, width = 1000, height = 130)
Top_frame.place(x=0, y=0)

#logo icon
logo_icon=PhotoImage(file="icon.png")
Label(Top_frame, image=logo_icon, bg=framebg).place(x=10, y=15)



Label(Top_frame,text="Text Tool", font=("Arial", 29)).place(x=110, y=30)

#Text area
text_area=Text(root,font="Roboto 20", bg="#cbd5e1", relief = GROOVE, wrap = WORD)
text_area.place(x=40, y = 150, width = 920, height = 250)

text_area2=Text(root,font="Roboto 20", bg="#cbd4d1", relief = GROOVE, wrap = WORD)
text_area2.place(x=40, y = 450, width = 920, height = 250)







root.mainloop()