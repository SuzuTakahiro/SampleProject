from tkinter import *
import tkinter.ttk as ttk

class TextSample(ttk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.createWidgets()
        self.pack()
    def createWidgets(self):
        text = Text(self)
        text.pack()

if __name__ == '__main__':
    master = Tk()
    master.title("TextSample")
    master.geometry("400x300")
    TextSample(master)
    master.mainloop()
