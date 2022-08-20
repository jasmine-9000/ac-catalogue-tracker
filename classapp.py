# TKinter shenanegans
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import filedialog
from utils import versioncheck


# OS imports
import os, sys

# Data imports
from wallpaper import wallpaper, wendell

from wallpaper_widget import WallpaperWidget2

class App:
    def __init__(self):
        if not versioncheck():
            sys.exit(1)
        self.root = Tk()
        print("instance created.")
    def run(self):
        print("instance ran.")

        
        self.w = wallpaper()
        self.wallpaperlist = WallpaperWidget2(self.root, "Wallpaper List", self.w)
        self.wallpaperlist.grid()

        self.ownedw = ["Ranch Wall"]
        self.ownedwallpaperlist = WallpaperWidget2(self.root, "Owned Wallpaper List", ["Ranch Wall"])
        self.ownedwallpaperlist.grid()
        
        unownedw = []
        
        for item in self.w:
            if item not in self.ownedw:
                unownedw.append(item)


        self.unownedw = unownedw
        self.unownedwallpaperlist = WallpaperWidget2(self.root, "Unowned Wallpaper List", self.unownedw)
        self.unownedwallpaperlist.grid()
        
        self.wallpaperinputstring = StringVar()

        self.wallpaperinputlabel = Label(self.root, text="Input your wallpapers here")
        self.wallpaperinputlabel.grid(column=1, row=0, sticky=(S))
        self.wallpaperinput = Entry(self.root, textvariable=self.wallpaperinputstring)
        self.wallpaperinput.grid(column=1, row=1, sticky=(N))
        self.wallpaperinputadd = Button(self.root, text="Add", command=self.updateOwnedAndUnownedWallpapers)
        self.root.bind('<Return>', lambda e: self.wallpaperinputadd.invoke())
        self.wallpaperinputadd.grid(column=1, row=2, sticky=(N))
        
        self.wendell = wendell()

        self.wendellwallpapersunowned = self.wendell
        for i in self.wendell:
            if i in self.ownedw:
                self.wendellwallpapersunowned.remove(i)
        self.wendellwallpapersunownedlist = WallpaperWidget2(self.root, "Unowned Wendell Wallpaper List",self.wendellwallpapersunowned)


        self.root.title("Hello Animal Crossing Catalogue")
        self.root.mainloop()
        
    def updateOwnedAndUnownedWallpapers(self, *args):
        s = self.wallpaperinputstring.get()
        if s in self.unownedw:
            print("Item in unowned wallpapers list. Adding...")
            self.unownedw.remove(s)
            self.unownedwallpaperlist.remove(s)
            self.ownedw.append(s)
            self.ownedwallpaperlist.add(s)
            return
        elif s in self.ownedw:
            print("Item already owned.")
            return
        else:
            print("Item not a wallpaper.")
        return
