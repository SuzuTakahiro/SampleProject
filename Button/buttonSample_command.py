from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as messagebox

class ButtonSampleCommand(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()
        self.pack()

    def create_widgets(self):
        button = ttk.Button(self,text = "button",command=self.showinfo)
        button.pack()
    def showinfo(self):
        messagebox.showinfo("info","buttonが押されました")


if __name__ == '__main__':
    master = Tk()
    master.title("ButtonSample-command")
    master.geometry("300x50")
    ButtonSampleCommand(master)
    master.mainloop()
