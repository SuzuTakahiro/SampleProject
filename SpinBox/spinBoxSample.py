from tkinter import *
import tkinter.ttk as ttk

class SpinBoxSample(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()
        self.pack()

    def create_widgets(self):
        spinbox = ttk.Spinbox(self)
        spinbox.pack()


if __name__ == '__main__':
    master = Tk()
    master.title("SpinBoxSample")
    master.geometry("300x50")
    SpinBoxSample(master)
    master.mainloop()
