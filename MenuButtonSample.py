from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as messagebox
import sys

class MenuButtonSample(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()
        self.pack()

    def create_widgets(self):
        menub = ttk.Menubutton(self,text='help')
        menu  = Menu(menub)
        menub['menu']= menu
        menu.add_command(label="python ver",command =self.pythonVer)
        menu.add_command(label="about app",command =self.about)
        menub.pack()

    def pythonVer(self):
        major = sys.version_info.major
        minor = sys.version_info.minor

        messagebox.showinfo("python version","お使いのPythonは{0}.{1}です。".format(major,minor))
    def about(self):
        messagebox.showinfo("info","メニューボタンのサンプルです")




if __name__ == '__main__':
    master = Tk()
    master.title("MenuButtonSample")
    master.geometry("300x100")
    MenuButtonSample(master)
    master.mainloop()
