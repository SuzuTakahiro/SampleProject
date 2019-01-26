from tkinter import *
import tkinter.ttk as ttk

class TreeViewSampleColumns(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()
        self.pack()

    def create_widgets(self):
        columns = ("column1","column2")
        self.tree = ttk.Treeview(self,columns=columns)
        self.tree.pack()
        # self.tree.heading("#0",text="アイコン列")
        # self.tree.heading("column1",text="column1")
        # self.tree.heading("column2",text="column2")


if __name__ == '__main__':
    master = Tk()
    master.title("TreeViewSampleColumns")
    master.geometry("700x250")
    TreeViewSampleColumns(master)
    master.mainloop()
