from tkinter import *
import tkinter.ttk as ttk

class TextSampleWidthHeight(ttk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.createWidgets()
        self.pack()
    def createWidgets(self):
        text = Text(self,width=10,height=2)
        text.pack()

if __name__ == '__main__':
    master = Tk()
    master.title("TextSampleWidthHeight")
    master.geometry("400x300")
    TextSampleWidthHeight(master)
    master.mainloop()
