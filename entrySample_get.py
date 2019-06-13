from tkinter import *
import tkinter.ttk as ttk

class EntrySampleGetValue(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.entry_variable = StringVar()
        self.createWidgets()
        self.pack()

    def createWidgets(self):
        self.entry = ttk.Entry(self,textvariable = self.entry_variable)
        self.entry.pack()
        button = ttk.Button(self,text="print",command=self.getEntryText)
        button.pack()

    def getEntryText(self):
        print("get variable:",self.entry_variable.get())
        print("get entry value:",self.entry.get())

if __name__ == '__main__':
    master = Tk()
    master.title("EntrySampleGetValue")
    master.geometry("300x50")
    EntrySampleGetValue(master)
    master.mainloop()
