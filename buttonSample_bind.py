from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as messagebox

class ButtonSampleBind(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()
        self.pack()

    def create_widgets(self):
        button = ttk.Button(self,text = "button")
        button.bind("<Button-1>",self.showinfo)
        button.pack()
    def showinfo(self,event):
        messagebox.showinfo("info","buttonが押されました")
        return "break"


if __name__ == '__main__':
    master = Tk()
    master.title("ButtonSample-Bind")
    master.geometry("300x50")
    ButtonSampleBind(master)
    master.mainloop()
