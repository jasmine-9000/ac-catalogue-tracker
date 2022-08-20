# TKinter shenanegans
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import filedialog



# OS imports
import os, sys

# Data imports
from wallpaper import wallpaper

# Widget imports 
from wallpaper_widget import wallpaper_widget, WallpaperWidget, WallpaperWidget2


# Functions

def donothing(root):
    filewin=Toplevel(root)
    button=Button(filewin, text="Do nothing button")
    button.pack()


def opensave():
    filetypes= (
        ('Text Files', '*.txt'),
        ('All Files', '*.*')
    )
    filename = filedialog.askopenfilename(title="Open Save", initialdir='/', filetypes=filetypes)
    showinfo(title='Selected Save File: ', message=filename)
    msg = ""
    if readfilesfromdialog and debug:
        with open(filename, "r") as fp:
            lines = fp.readlines()
            for x in lines:
                msg += x
        showinfo(title='Contents: ', message=msg)

def newWindow(parent, widgetframe, name="Default Name"):
    newWin = Toplevel(parent)
    newWin.title(name)
    widgetframe.master = parent
    widgetframe.grid(column=0, row=0)


# debug options
debug = True
readfilesfromdialog = False

def run():
    #python version check.
    cont = False
    if sys.version_info < (3,0,0):
        sys.stderr.write("You must have Python 3 to run this scrypt")
        sys.exit(1)
    elif sys.version_info < (3,2,0):
        c = input("Python 3.2 is recommended for this script. Continue?(y/n)")
        if c == 'y': 
            cont = True
        if not cont:
            sys.exit(1)


    # init tkinter
    root = Tk() # create root window
    menubar = Menu(root) # create menu bar
    filemenu = Menu(menubar, tearoff=0) # create file menu
    filemenu.add_command(label="New", command=donothing)
    filemenu.add_command(label="Open", command=opensave)
    filemenu.add_command(label="Save", command=donothing(root))
    filemenu.add_command(label="Close", command=donothing)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=filemenu)

    testmenu = Menu(menubar, tearoff=0)
    testmenu.add_command(label="Test 1", command=newWindow(root, WallpaperWidget(root, "Saharah wallpaper", "x")))
    menubar.add_cascade(label="Test", menu=testmenu)

    root.config(menu=menubar)
    frm = ttk.Frame(root, padding=10) # create a frame widget
    frm.master.title("Animal Crossing Catalogue Tracker")

    # create the grid in the main frame
    frm.grid()
    # create label
    ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
    
    wallpaper_widget(root, wallpaper())

    www = WallpaperWidget(root, "Saharah wallpaper", "x")
    www.grid(row=1, column=1, sticky=(N,E))

    newWindow1 = Toplevel(root)
    www3 = WallpaperWidget2(newWindow1, "All Wallpapers Owned", ("X", "Y", "Z"))
    www3.grid()
    #ttk.Label(frm, text = )).grid(column=0, row=1)
    #tkk.Button(frm, text="Open File", command=root.tk.createfilehandler()).grid(row=1)
    #ttk.Button(frm, text="Open File", command=root.tk.deletefilehandler()).grid(row=1)


    #start main loop
    root.mainloop()