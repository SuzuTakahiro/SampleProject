from tkinter import *
import tkinter.ttk as ttk

class TreeViewSample(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()
        self.pack()

    def create_widgets(self):
        self.tree = ttk.Treeview(self)
        self.tree.pack()


if __name__ == '__main__':
    master = Tk()
    master.title("TreeViewSample")
    master.geometry("300x250")
    TreeViewSample(master)
    master.mainloop()
