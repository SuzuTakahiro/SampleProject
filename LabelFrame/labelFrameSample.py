from tkinter import *
import tkinter.ttk as ttk


class LabelFrameSample(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()
        self.pack()

    def create_widgets(self):
        labelFrame  = ttk.LabelFrame(self,text="labelFrame")
        labelFrame.pack()

        ttk.Label(labelFrame,text="LabelFrameSample").pack()

if __name__ == '__main__':
    master = Tk()
    master.title("LabelFrameSample")
    master.geometry("300x50")
    LabelFrameSample(master)
    master.mainloop()
