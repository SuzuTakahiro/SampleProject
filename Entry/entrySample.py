from tkinter import *
import tkinter.ttk as ttk

class EntrySample(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()
        self.pack()

    def create_widgets(self):
        entry = ttk.Entry(self)
        entry.pack()


if __name__ == '__main__':
    master = Tk()
    master.title("EntrySample")
    master.geometry("300x50")
    EntrySample(master)
    master.mainloop()
