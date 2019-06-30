from tkinter import *
import tkinter.ttk as ttk

class ComboboxValuesSample(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()
        self.pack()

    def create_widgets(self):
        valuelist=["ぶどう","バナナ","もも","いちご"]
        combo = ttk.Combobox(self,values=valuelist)
        combo.pack()


if __name__ == '__main__':
    master = Tk()
    master.title("ComboboxValuesSample")
    master.geometry("300x200")
    ComboboxValuesSample(master)
    master.mainloop()
