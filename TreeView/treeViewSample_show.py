from tkinter import *
import tkinter.ttk as ttk

class TreeViewSampleHeading(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()
        self.setHeader()
        self.setData()
        self.pack()

    def create_widgets(self):
        self.tree = ttk.Treeview(self)
        self.tree.pack()

    def setHeader(self):
        columns =("name","value")
        self.tree["columns"]=columns
        for col in columns:
            self.tree.heading(col,text=col)
    def setData(self):
        datalist=[("orange",100),("apple",120)]
        for data in datalist:
            self.tree.insert("",index="end",text="sample data",values=data)


if __name__ == '__main__':
    master = Tk()
    master.title("TreeViewSampleHeading")
    master.geometry("700x250")
    TreeViewSampleHeading(master)
    master.mainloop()
