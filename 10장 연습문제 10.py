from tkinter import *
from tkinter.filedialog import *
from tkinter.simpledialog import *

def func_open():
    global filename
    filename = askopenfilename(parent = window, filetypes = (("GIF 파일", "*.gif"),
                ("모든 파일", "*.*")))
    photo = PhotoImage(file = filename)
    pLabel.configure(image = photo)
    pLabel.image = photo

def func_exit():
    window.quit()
    window.destroy() 

def func_zoom():
    value = askinteger("확대배수","확대할 배수를 선택(1~10)",minvalue = 1,maxvalue = 10)
    photo = PhotoImage(file = filename)
    photo = photo.zoom(value,value)
    pLabel.configure(image = photo)
    pLabel.image = photo

def func_subsample():
    value = askinteger("축소배수","축소할 배수를 선택(1~10)",minvalue = 1,maxvalue = 10)
    photo = PhotoImage(file = filename)
    photo = photo.subsample(value,value)
    pLabel.configure(image = photo)
    pLabel.image = photo

window = Tk()
window.geometry("500x500")
window.title("명화 감상하기")

photo = PhotoImage()
pLabel = Label(window,image = photo)
pLabel.pack(expand = 1, anchor = CENTER)

mainMenu = Menu(window)
window.config(menu = mainMenu)
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = '파일',menu = fileMenu)
fileMenu.add_command(label = '파일 열기', command = func_open)
fileMenu.add_separator()
fileMenu.add_command(label = '프로그램 종료', command = func_exit)

imageMenu = Menu(mainMenu)
imageMenu.add_command(label = '확대하기', command = func_zoom)
imageMenu.add_separator()
imageMenu.add_command(label = '축소하기', command = func_subsample) 

window.mainloop()
