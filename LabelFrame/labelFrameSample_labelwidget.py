from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as messagebox


#labelwidget
class LabelFrameSampleLabelWidget(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()
        self.pack()

    def create_widgets(self):
        button = ttk.Button(self,text="button",command=self.showMessage)
        labelFrame  = ttk.LabelFrame(self,labelanchor="nw",labelwidget=button,width=280,height=180)
        labelFrame.pack()

    def showMessage(self):
        messagebox.showinfo("infomation", "ラベルが押された")

if __name__ == '__main__':
    master = Tk()
    master.title("LabelFrame-labelwidget")
    master.geometry("300x200")
    LabelFrameSampleLabelWidget(master)
    master.mainloop()
