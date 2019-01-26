from tkinter import *
import tkinter.ttk as ttk

class FrameSampleWinfoChildren(ttk.Frame):


    def __init__(self, master):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        firstFrame =ttk.Frame(self)
        firstFrame.pack()

        mkbutton = ttk.Button(self,text="make",command = lambda:self.make_child(firstFrame))
        mkbutton.pack(side="left")

        dbutton = ttk.Button(self,text="destroy",command = lambda:self.destroy_child(firstFrame))
        dbutton.pack(side="left")

    def destroy_child(self,frame):
        children = frame.winfo_children()
        print(children)
        for child in children:
            child.destroy()

    def make_child(self,frame):
        label0 = ttk.Label(frame,text="Sample0")
        label0.pack()
        label1 = ttk.Label(frame,text="Sample1")
        label1.pack()
        label2 = ttk.Label(frame,text="Sample2")
        label2.pack()





if __name__ == '__main__':
    master  = Tk()
    master.geometry("600x400")
    master.title("FrameSampleWinfoChildren")
    FrameSampleWinfoChildren(master)
    master.mainloop()
