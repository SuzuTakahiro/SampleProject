from tkinter import *
import tkinter.ttk as ttk

class VariableSample(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.int_var = IntVar(value=0)
        self.double_var = DoubleVar(value=0.0)
        self.boolean_var = BooleanVar(value=True)
        self.string_var = StringVar(value="string")
        self.create_widgets()
        self.pack()

    def create_widgets(self):
        intSpin = ttk.Spinbox(self,textvariable=self.int_var)
        intSpin.pack()

        doubleSpin = ttk.Spinbox(self,textvariable=self.double_var)
        doubleSpin.pack()

        booleanCheck =ttk.Checkbutton(self,text = "test",variable=self.boolean_var)
        booleanCheck.pack()

        stringEntry = ttk.Entry(self,textvariable = self.string_var)
        stringEntry.pack()

        buttonframe = ttk.Frame(self)
        buttonframe.pack()

        inButton = ttk.Button(buttonframe,text="input",command=self.inputValue)
        inButton.pack(side="left")

        outButton = ttk.Button(buttonframe,text="output",command=self.outputValue)
        outButton.pack(side="left")


    def inputValue(self):
        self.int_var.set(1)
        self.double_var.set(0.1)
        self.boolean_var.set(False)
        self.string_var.set("sample")

    def outputValue(self):
        print(self.int_var.get())
        print(self.double_var.get())
        print(self.boolean_var.get())
        print(self.string_var.get())




if __name__ == '__main__':
    master = Tk()
    master.title("VariableSample")
    master.geometry("300x400")
    VariableSample(master)
    master.mainloop()
