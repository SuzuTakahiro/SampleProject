from tkinter import *
import tkinter.ttk as ttk

class CheckButtonSampleVariable(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.int_value = IntVar()
        self.create_widgets()
        self.pack()


    def create_widgets(self):

        checkbutton = ttk.Checkbutton(self,text = "checkbutton",variable=self.int_value)
        checkbutton.pack()

        label = ttk.Label(self,textvariable=self.int_value)
        label.pack()


if __name__ == '__main__':
    master = Tk()
    master.title("CheckButtonSample-variable")
    master.geometry("350x50")
    CheckButtonSampleVariable(master)
    master.mainloop()
