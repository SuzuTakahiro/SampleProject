from tkinter import *
import tkinter.ttk as ttk

class TextSampleBlockCursor(ttk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.createWidgets()
        self.pack()
    def createWidgets(self):
        text = Text(self,blockcursor=True)
        text.pack()

if __name__ == '__main__':
    master = Tk()
    master.title("TextSampleBlockCursor")
    master.geometry("400x300")
    TextSampleBlockCursor(master)
    master.mainloop()
