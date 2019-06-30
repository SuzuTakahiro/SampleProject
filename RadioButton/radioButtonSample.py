from tkinter import *
import tkinter.ttk as ttk

class RadioButtonSample(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()
        self.pack()

    def create_widgets(self):
        radio = ttk.Radiobutton(self,text = "radiobutton")
        radio.pack()


if __name__ == '__main__':
    master = Tk()
    master.title("RadioButtonSample")
    master.geometry("300x50")
    RadioButtonSample(master)
    master.mainloop()
