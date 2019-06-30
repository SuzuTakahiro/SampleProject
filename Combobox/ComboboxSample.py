from tkinter import *
import tkinter.ttk as ttk

class ComboboxSample(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()
        self.pack()

    def create_widgets(self):
        combo = ttk.Combobox(self,values="sample")
        combo.pack()


if __name__ == '__main__':
    master = Tk()
    master.title("ComboboxSample")
    master.geometry("300x50")
    ComboboxSample(master)
    master.mainloop()
