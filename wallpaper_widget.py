# TKinter shenanegans
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import filedialog


class WallpaperWidget(Frame):
    def __init__(self, parent, label, default=""):
        Frame.__init__(self, parent)
        
        self.label = Label(self, text=label, anchor="w")

        
        # trace the string variable. 
        self.sv = StringVar()
        self.sv.trace("w", lambda name, index, mode, sv = self.sv: self.callback(self.sv))
        self.entry = Entry(self, textvariable=self.sv)
        self.entry.insert(0, default)

        self.label.pack()
        self.entry.pack()
          
    def callback(self, *args):
        print(self.sv.get())

    def get(self):
        return self.entry.get()



def wallpaper_widget(root, wallpaper_data):
    mylist = Listbox(root)
    for w in wallpaper_data:
        mylist.insert(END, w)
    mylist.grid(column=0,row=1, padx = (10,0), pady = (10,0))
    # create scrollbar for all the wallpapers
    scrollbar = Scrollbar(root, orient=VERTICAL, command=mylist.yview)
    scrollbar.grid(column=0, row=1, sticky=(N,S,E))
    mylist['yscrollcommand'] = scrollbar.set
    wallpaper_label = Label(root, text="All Wallpapers").grid(column=0, row=2, columnspan=2, sticky=(W,E))


class WallpaperWidget2(Frame):
    def __init__(self, parent, label, itemslist):
        Frame.__init__(self, parent)
        
        self.title = Label(self, text=label, anchor='w')
        self.itemslist = Listbox(self)
        for item in itemslist:
            self.itemslist.insert(END, item)
        self.title.grid(column=0, row=0)
        self.itemslist.grid(column=0, row=1)
          
    def callback(self, *args):
        print(self.sv.get())
    
    def hello(self, *args):
        pass
    def remove(self, item):
        #self.itemslist.remove(item)
        idx = self.itemslist.get(0, END).index(item)
        self.itemslist.delete(idx)
        

    def add(self, item):
        self.itemslist.insert(END, item)
