from tkinter import *
import tkinter.ttk as ttk

class ComboboxSampleVariableOption(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.variable = StringVar()
        self.create_widgets()
        self.pack()

    def create_widgets(self):
        valuelist=["ぶどう","バナナ","もも","いちご"]
        self.combo = ttk.Combobox(self,values=valuelist,textvariable=self.variable)
        self.combo.pack()
        button = ttk.Button(self,text="print",command= self.printValue)
        button.pack()
    def printValue(self):
        print(self.variable.get())
        print(self.combo.get())


if __name__ == '__main__':
    master = Tk()
    master.title("ComboboxSampleVariableOption")
    master.geometry("350x200")
    ComboboxSampleVariableOption(master)
    master.mainloop()
