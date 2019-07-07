from tkinter import *
import tkinter.ttk as ttk

class JobManagerView(ttk.Frame):
    def __init__(self,master):
        super().__init__(master,borderwidth="20px")
        self.createWidgets()
    def createWidgets(self):
        JobExecWidget(self).pack()
        for i in range(5):
            JobWidget(self,"Job {0}".format(i)).pack()
        self.pack()
class JobExecWidget(ttk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.createWidgets()
    def createWidgets(self):
        ttk.Label(self,text="Parallel Job").pack(side="left")
        ttk.Spinbox(self,from_=1,to=4,value=0).pack(side="left")
        ttk.Button(self,text="Exec").pack(side="left")

class JobWidget(ttk.Frame):
    def __init__(self,master,text="job"):
        super().__init__(master)
        self.createWidgets(text)
    def createWidgets(self,text):
        label = ttk.Label(self,text=text)
        label.grid(column=0,row=0)
        button = ttk.Button(self,text="command",command=lambda:CommandWidget(self))
        button.grid(column=1,row=0)
        progressbar = ttk.Progressbar(self,length = 400,orient="horizontal",value=40)
        progressbar.grid(column=2,row=0)

class CommandWidget(Toplevel):
    def __init__(self,master):
        super().__init__(master)
        self.title("InputCommand")
        self.geometry("300x200")
        self.createWidgets()
    def createWidgets(self):
        frame = ttk.Frame(self,borderwidth="10px")
        frame.pack()
        ttk.Label(frame,text="command").pack(side="left")
        ttk.Entry(frame).pack(side="left")


if __name__ == '__main__':
    master = Tk()
    master.geometry("800x600")
    master.title("JobManagerSample")
    JobManagerView(master)
    master.mainloop()
