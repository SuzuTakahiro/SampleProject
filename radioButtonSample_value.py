from tkinter import *
import tkinter.ttk as ttk

class RadioButtonSampleValue(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        # 初期値はyesが押された状態にする
        self.str_var = StringVar(value="yes")
        self.create_widgets()
        self.pack()


    def create_widgets(self):

        valueLabel = ttk.Label(self,textvariable=self.str_var)
        valueLabel.pack()

        yesRadio = ttk.Radiobutton(self,text = "yes",value="yes",variable=self.str_var)
        yesRadio.pack(side="left")
        noRadio = ttk.Radiobutton(self,text = "no",value="no",variable=self.str_var)
        noRadio.pack(side="left")


if __name__ == '__main__':
    master = Tk()
    master.title("RadioButtonSample")
    master.geometry("300x50")
    RadioButtonSampleValue(master)
    master.mainloop()
