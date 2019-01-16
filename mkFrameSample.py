from tkinter import *
import tkinter.ttk as ttk


class FrameSample:

    def __init__(self, master):
        frame = ttk.Frame(master)
        frame.pack()


if __name__ == '__main__':
    master = Tk()
    master.title("FrameSample")
    master.geometry("300x50")
    FrameSample(master)
    master.mainloop()
