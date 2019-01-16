from tkinter import *
import tkinter.ttk as ttk

#propagate-True
class LabelFrameSamplePropagateTrue(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()
        self.pack()

    def create_widgets(self):
        labelFrame  = ttk.LabelFrame(self,text="propagate-True",labelanchor="nw",width=280,height=180)
        labelFrame.pack()
        labelFrame.propagate(True)

        # child-widget
        label = ttk.Label(labelFrame, text ="propagate true")
        label.pack()
        button = ttk.Button(labelFrame, text ="True")
        button.pack()

# propagate-False
class LabelFrameSamplePropagateFalse(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()
        self.pack()

    def create_widgets(self):
        labelFrame  = ttk.LabelFrame(self,text="propagate-False",labelanchor="nw",width=280,height=180)
        labelFrame.pack()
        labelFrame.propagate(False)
        label = ttk.Label(labelFrame, text ="propagate false")
        label.pack()
        button = ttk.Button(labelFrame, text ="False")
        button.pack()


if __name__ == '__main__':
    master = Tk()
    master.title("LabelFrame-propagate")
    master.geometry("300x300")
    LabelFrameSamplePropagateTrue(master)
    LabelFrameSamplePropagateFalse(master)

    master.mainloop()
