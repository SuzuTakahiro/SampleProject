from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as messagebox

class ButtonSampleCommandLambda(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()
        self.pack()

    def create_widgets(self):
        button = ttk.Button(self,text = "button",command=lambda:self.showinfo(text="ボタンが押されました"))
        button.pack()

    def showinfo(self,text="messeage"):
        messagebox.showinfo("info",text)


if __name__ == '__main__':
    master = Tk()
    master.title("ButtonSample-command-lambda")
    master.geometry("350x50")
    ButtonSampleCommandLambda(master)
    master.mainloop()
