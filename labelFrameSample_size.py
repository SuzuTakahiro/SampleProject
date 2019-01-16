from tkinter import *
import tkinter.ttk as ttk

#propagate-True
class LabelFrameSampleWidthHeight(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()
        self.pack()

    def create_widgets(self):
        labelFrame  = ttk.LabelFrame(self,text="Size",labelanchor="nw",width=280,height=180)
        labelFrame.pack()


if __name__ == '__main__':
    master = Tk()
    master.title("LabelFrame-Size")
    master.geometry("300x200")
    LabelFrameSampleWidthHeight(master)

    master.mainloop()
