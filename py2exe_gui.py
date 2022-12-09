#!usr/bin/env python
from lib2to3.pgen2.token import COMMA
from tkinter import *
from tkinter.font import BOLD
from tkinter import Tk, Menu, filedialog
from tkinter.messagebox import *
from tkinter.filedialog import *
from tkinter.messagebox import showinfo
import os
import subprocess
import time

command = ["pyinstaller --noconfirm", "--onefile", "--console","--windowed", "--icon"]
out = "output : "
os.system("title output -- Py 2 EXE ( by iniyavan)")
print(out)

def console():

    _console = command[2]
    file = location_.get()
    if file == "" or file == " ":
        location_.insert(0,"enter valid path")
    else:
        _file = f'"{file}"'

    a_ = icon_.get()
    print(a_)
    if a_ == "" or a_ == " ":
        command_pass = f"{command[0]} {command[1]} {_console} {_file}"
    else:
        ico_ = command[4]
        _ico = f'"{a_}"'
        command_pass = f"{command[0]} {command[1]} {_console} {ico_} {_ico} {_file}"
    print(command_pass)
    compaile_.insert(0, "Compailing...")
    flag = True
    if flag == True:
            time.sleep(3)
            execute = subprocess.check_output(command_pass, shell=True, universal_newlines=True)
            print(out)
            compaile_.delete(0, END)
            compaile_.insert(0, "--compailed--")
            print("\n\t_______compailed_________")
            flag = False

    output = out_folder.get()

    if output == "" or output == " ":
        out_folder.insert(0, "enter a valid path")
    else:
        if flag == False:
            os.system(f'move "dist\*.exe" "{output}"')
            os.system(f'del "*.spec"')
            os.system(f'rmdir /S /Q "build"')
            os.system(f'rmdir /Q "dist"')

def windowed():

    _console = command[3]
    file = location_.get()
    if file == "" or file == " ":
        location_.insert(0,"enter valid path")
    else:
        _file = f'"{file}"'

    a_ = icon_.get()
    print(a_)
    if a_ == "" or a_ == " ":
        command_pass = f"{command[0]} {command[1]} {_console} {_file}"
    else:
        ico_ = command[4]
        _ico = f'"{a_}"'
        command_pass = f"{command[0]} {command[1]} {_console} {ico_} {_ico} {_file}"
    print(command_pass)
    compaile_.insert(0, "Compailing...")
    flag = True
    if flag == True:
            time.sleep(3)
            execute = subprocess.check_output(command_pass, shell=True, universal_newlines=True)
            print(out)
            compaile_.delete(0, END)
            compaile_.insert(0, "--- compailed ---")
            print("\n\t_______compailed_________")
            flag = False

    output = out_folder.get()

    if output == "" or output == " ":
        out_folder.insert(0, "enter a valid path")
    else:
        if flag == False:
            os.system(f'move "dist\*.exe" "{output}"')
            os.system(f'del "*.spec"')
            os.system(f'rmdir /S /Q "build"')
            os.system(f'rmdir /Q "dist"')

def clear_all() :
    location_.delete(0, END)
    icon_.delete(0, END)
    out_folder.delete(0, END)
    compaile_.delete(0, END)
    location_.focus_set()
    os.system("cls")
    print(out)

def browse():
    py_exts = r"*.py  *.py3 *.pyc  *.pyo  *.pyw  *.pyx  *.pyd  *.pxd  *.pyi  *.pyi  *.pyz  *.pywz *.rpy  *.pyde *.pyp  *.pyt  *.xpy  *.ipynb"
    fileopen = askopenfilename(defaultextension=".py",
                                      filetypes=[("Python Files",py_exts),("All Files","*.*")])
    location_.insert(0,fileopen)

def brwose_ico():
    fileopenn = askopenfilename(filetypes=[("Image files","*.ico"),("All Files","*.*")])
    icon_.insert(0,fileopenn)

def folder():
    fileopennn = filedialog.askdirectory(title="Dialog box")
    out_folder.insert(0,fileopennn)

def about():
	abou_t=Tk()
	abou_t.iconbitmap('./icon_.ico')
	abou_t.configure(background = 'white')
	abou_t.geometry("560x565")
	abou_t.title("About")

	lbb1 = Label(abou_t, text = "\nPY 2 EXE --V1.0\n_________________________",
				fg = 'blue', bg='white',bd = 1, anchor = "w",font = ('conlas', 20, 'bold'))
	lbb2 = Label(abou_t, text = "\nVersion 1.0\nCopyright © 2022. All rights reserved.\n\tGNU Genral Public License.\n\nThis program is free software; you can redistribute it \nand/or modify it under the terms of the GNU General\n Public License as published by the Free Software     `\nFoundation;                                                               `\n\nThis program is distributed in the hope that it will be \n  useful, but WITHOUT ANY WARRANTY; without even \n  the implied warranty of MERCHANTABILITY or FITNESS\nFOR A PARTICULAR PURPOSE. See the GNU General\n  Public License for more details.                                     `\nYou should have received a copy of the GNU General \nPublic License along with this program. If not, see \n<https://www.gnu.org/licenses/>.",
				fg = 'black', bg='white',bd = 1, anchor = "w",font = ('conlas', 12, 'bold'))
	lbb1.grid(row=0,column=1)
	lbb2.grid(row=1,column=1)

if __name__ == "__main__" :
    from PIL import ImageTk, Image
    root = Tk()
    root.configure(background = 'white')
    root.geometry("880x730")
    root.title("Py 2 Exe -- V1.0")
    root.iconbitmap('./icon_.ico')
    menubar = Menu(root)
    
    #-----------------------------------LABEL--------------------------------------------#
    frame = Frame(root, width=50, height=10)
    frame.pack()
    img = ImageTk.PhotoImage(Image.open(".\icon_1.bmp"))
    label = Label(frame, image = img)
    label.pack()
    frame.place(x=300,y=35)
    lbl = Label(root,font = ('helvetica', 20, 'bold'),
		text = "Py 2 EXE",bg="white",fg = "blue", bd = 10, anchor='w')
    lbl.place(x=380, y=35)

    #-----------------------------------script-------------------------------------------#
    label1 = Label(root, text = "Script Location : ",
				fg = 'black', bg='white',bd = 1, anchor = "w",font = ('conlas', 12, 'bold'))
    label1.place(x=60, y=180)
    
    location_ = Entry(root, font = ('arial', 10),bd = 1, insertwidth = 2,fg="blue",
				bg = "#D5D6D4", justify = 'left')
    location_.place(x=309,y=180, width=400, height=30)

    button1 = Button(root, text = "browse", bg = "blue",fg = "white", command =browse,
					bd = 0, anchor = "w",font = ('conolas', 10, 'bold'),pady = 0, padx = 1)
    button1.place(x=723,y=180)

    #----------------------------------icon------------------------------------------------#

    label2 = Label(root, text = "Icon Location (optional): ",
				fg = 'black', bg='white',bd = 1, anchor = "w",font = ('conlas', 12, 'bold'))
    label2.place(x=60, y=260)
    
    icon_ = Entry(root, font = ('arial', 10),bd = 1, insertwidth = 2,fg="blue",
				bg = "#D5D6D4", justify = 'left')
    icon_.place(x=310,y=260, width=400, height=30)

    button2 = Button(root, text = "browse", bg = "blue",fg = "white", command = brwose_ico,
					bd = 0, anchor = "w",font = ('conolas', 10, 'bold'),pady = 0, padx = 1)
    button2.place(x=725,y=260)

    #------------------------------------output folder------------------------------------#

    label3 = Label(root, text = "output folder (must) : ",
				fg = 'black', bg='white',bd = 1, anchor = "w",font = ('conlas', 12, 'bold'))
    label3.place(x=60, y=330)
    
    out_folder = Entry(root, font = ('arial', 10),bd = 1, insertwidth = 2,fg="blue",
				bg = "#D5D6D4", justify = 'left')
    out_folder.place(x=310,y=330, width=400, height=30)

    button3 = Button(root, text = "browse", bg = "blue",fg = "white", command = folder,
					bd = 0, anchor = "w",font = ('conolas', 10, 'bold'),pady = 0, padx = 1)
    button3.place(x=725,y=330)

    #--------------------------------------buttons------------------------------------#
    buttonexee = Button(root, text = "Clear ", bg = "#E8E81A",fg = "blue", command = clear_all,
					bd = 0, anchor = "w",font = ('conolas', 10, 'bold'),pady = 30, padx = 341)
    buttonexee.place(x=60,y=540)

    buttonexe = Button(root, text = "   Console", bg = "blue",fg = "#E8E81A", command = console,
					bd = 0, anchor = "w",font = ('conolas', 10, 'bold'),pady = 30, padx = 135)
    buttonexe.place(x=60,y=450)

    buttonexe = Button(root, text = "WINDOWED", bg = "blue",fg = "#E8E81A", command = windowed,
					bd = 0, anchor = "w",font = ('conolas', 10, 'bold'),pady = 30, padx = 135)
    buttonexe.place(x=420,y=450)

    #---------------------------------------compaile-----------------------------------#
    
    compaile_ = Entry(root, font = ('arial', 20),bd = 0, insertwidth = 0,fg="blue",
				bg = "white", justify = 'left')
    compaile_.place(x=320,y=400, width=400, height=35)

    lbl3 = Label(root, font = ('helvetica', 10, 'bold'),
                text = "\ncreated by iniyavan.\ncopyright © 2021, v2.1.5 build 5.1",bg="white",fg = "black",)
    lbl3.place(x=300,y=630)
    #----------------------------------------------------------------------------------#
  
    root.mainloop()

# In[]:
print("created by iniyavan")
print("D3XT3R")
