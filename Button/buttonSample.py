from tkinter import *
import tkinter.ttk as ttk

class ButtonSample(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()
        self.pack()

    def create_widgets(self):
        button = ttk.Button(self,text = "button")
        button.pack()


if __name__ == '__main__':
    master = Tk()
    master.title("ButtonSample")
    master.geometry("300x50")
    ButtonSample(master)
    master.mainloop()
