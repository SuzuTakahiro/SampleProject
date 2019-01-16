from tkinter import *
import tkinter.ttk as ttk

class CheckButtonSample(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()
        self.pack()

    def create_widgets(self):
        checkbutton = ttk.Checkbutton(self,text = "checkbutton")
        checkbutton.pack()


if __name__ == '__main__':
    master = Tk()
    master.title("CheckButtonSample")
    master.geometry("300x50")
    CheckButtonSample(master)
    master.mainloop()
