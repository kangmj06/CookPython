from tkinter import *
from tkinter import ttk

window=Tk()
window.iconbitmap('CookPython.ico')

baseTab=ttk.Notebook(window)

Notebook=tkinter.ttk.Notebook(window, width=520, height=180)
Notebook.place(x=15, y= 350)

tabDog=ttk.Frame(baseTab)
baseTab.add(tabDog,text="강아지")
tabCat=ttk.Frame(baseTab)
baseTab.add(tabCat,text="고양이")

#2021041040 강문정 
baseTab.pack(expand=1,fill="both")

 
photoDog=PhotoImage(file="C:\CookPython\gif/dog3.gif")
labelDog=Label(tabDog,image=photoDog)
labelDog.pack()

 
photoCat=PhotoImage(file="C:\CookPython\gif/cat.gif")
labelCat=Label(tabCat,image=photoCat)
labelCat.pack()

window.mainloop()
