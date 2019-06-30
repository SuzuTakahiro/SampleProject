from tkinter import *
import tkinter.ttk as ttk

class LabelSampleBackground(ttk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()
        self.pack()

    def create_widgets(self):
        label = ttk.Label(self,text="label",background="#ff0000")
        label.pack()

if __name__ == '__main__':
    master = Tk()
    master.title("LabelSampleBackground")
    master.geometry("300x50")
    LabelSampleBackground(master)
    master.mainloop()
