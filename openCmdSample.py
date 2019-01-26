from tkinter import *
import tkinter.ttk as ttk
import subprocess

class OpenCmdSample(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()
        self.pack()

    def create_widgets(self):
        button = ttk.Button(self,text = "button",command=self.openCmd)
        button.pack()
    def openCmd(self):
        command ="cmd.exe /c start"
        subprocess.Popen(command)



if __name__ == '__main__':
    master = Tk()
    master.title("OpenCmdSample")
    master.geometry("300x50")
    OpenCmdSample(master)
    master.mainloop()
