from tkinter import *
import tkinter.ttk as ttk

class SpinBoxSampleFromTo(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()
        self.pack()

    def create_widgets(self):
        spinbox = ttk.Spinbox(self,from_=0,to=10)
        spinbox.pack()


if __name__ == '__main__':
    master = Tk()
    master.title("SpinBoxSample-FromTo")
    master.geometry("300x50")
    SpinBoxSampleFromTo(master)
    master.mainloop()
