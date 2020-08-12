from tkinter import *
from tkinter import filedialog as fd
import os
from tkinter.messagebox import *

root=Tk()
root.title("Notepad")
root.geometry("600x400")

# Functions


def quitProgram():
    quit()


def openFile():
    name = fd.askopenfile()


def newFile():
    pass


def saveFile():
    pass


def saveAsFile():
    name = fd.asksaveasfile(mode="w",defaultextension=".txt")


def about():
    showinfo("About","This is notepad on tkinter by shanu")

menu = Menu(root)
root.config(menu=menu)
file=Menu(menu)
file.add_command(label="New",command=newFile)
file.add_command(label="Open",command=openFile)
file.add_command(label="Save",command=saveFile)
file.add_command(label="Save as",command=saveAsFile)
file.add_command(label="Exit",command=quitProgram)
menu.add_cascade(label="File",menu=file)

root.config(menu=menu)
edit=Menu(menu)
edit.add_command(label="Format")
edit.add_command(label="Font size")
menu.add_cascade(label="Edit",menu=edit)


root.config(menu=menu)
help=Menu(menu)
help.add_command(label="Help")
help.add_command(label="About",command=about)
menu.add_cascade(label="Help",menu=help)

text = Text(root)
text.grid(row=0,column=0)
root.mainloop()
