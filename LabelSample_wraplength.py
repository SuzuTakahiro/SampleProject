from tkinter import *
import tkinter.ttk as ttk

class LabelSampleWrapLength(ttk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()
        self.pack()

    def create_widgets(self):
        label = ttk.Label(self,text="labellabellabel",wraplength=25)
        label.pack()

if __name__ == '__main__':
    master = Tk()
    master.title("LabelSampleWrapLength")
    master.geometry("300x50")
    LabelSampleWrapLength(master)
    master.mainloop()
