import tkinter.ttk as ttk
from tkinter import *
from uiBuilderView import UIBuilderApp




if __name__ == '__main__':
    master = Tk()
    master.title("UIBuilder")
    master.geometry("800x600")
    UIBuilderApp(master)
    master.mainloop()
