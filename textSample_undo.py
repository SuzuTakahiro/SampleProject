from tkinter import *
import tkinter.ttk as ttk

class TextSampleUndoRedo(ttk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.createWidgets()
        self.pack()
    def createWidgets(self):
        text = Text(self,undo=True)
        text.pack()

if __name__ == '__main__':
    master = Tk()
    master.title("TextSampleUndoRedo")
    master.geometry("400x300")
    TextSampleUndoRedo(master)
    master.mainloop()
