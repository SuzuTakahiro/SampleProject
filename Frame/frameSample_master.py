from tkinter import *
import tkinter.ttk as ttk

class FrameSampleParent(ttk.Frame):


    def __init__(self, master):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        parentFrame =ttk.LabelFrame(self,text="parentframe",width="200",height="200")
        parentFrame.pack()
        parentFrame.propagate(False)

        updateButton = ttk.Button(parentFrame,text="update")
        updateButton.pack()
        updateButton.bind("<Button-1>",self.updateParentSize)

    def updateParentSize(self,event):
        parent  = event.widget.master
        print("width:{},height:{}".format(parent['width'],parent['height']))
        parent['width']  ="300"
        parent['height']= "300"







if __name__ == '__main__':
    master  = Tk()
    master.geometry("600x400")
    master.title("FrameSampleParent")
    FrameSampleParent(master)
    master.mainloop()
