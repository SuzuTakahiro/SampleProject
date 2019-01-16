from tkinter import *
import tkinter.ttk as ttk

class CheckButtonSampleOnOffValue(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.str_value = BooleanVar()
        self.create_widgets()
        self.pack()


    def create_widgets(self):
        self.str_value.set("on")
        checkbutton = ttk.Checkbutton(self,text = "checkbutton",variable=self.str_value,onvalue=True,offvalue=False)
        checkbutton.pack()

        label = ttk.Label(self,textvariable=self.str_value)
        label.pack()


if __name__ == '__main__':
    master = Tk()
    master.title("CheckButtonSample-onoffvalue")
    master.geometry("350x50")
    CheckButtonSampleOnOffValue(master)
    master.mainloop()
