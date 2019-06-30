from tkinter import *
import tkinter.ttk as ttk

# north-west
class LabelFrameSampleNW(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()
        self.pack()

    def create_widgets(self):
        nwLabelFrame  = ttk.LabelFrame(self,text="nw-sample",labelanchor="nw",width=280,height=180)
        nwLabelFrame.pack()
        nwLabelFrame.propagate(False)
# north
class LabelFrameSampleN(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()
        self.pack()

    def create_widgets(self):
        nwLabelFrame  = ttk.LabelFrame(self,text="n-sample",labelanchor="n",width=280,height=180)
        nwLabelFrame.pack()
        nwLabelFrame.propagate(False)

# north-east
class LabelFrameSampleNE(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()
        self.pack()

    def create_widgets(self):
        nwLabelFrame  = ttk.LabelFrame(self,text="ne-sample",labelanchor="ne",width=280,height=180)
        nwLabelFrame.pack()
        nwLabelFrame.propagate(False)
# east-north
class LabelFrameSampleEN(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()
        self.pack()

    def create_widgets(self):
        nwLabelFrame  = ttk.LabelFrame(self,text="en-sample",labelanchor="en",width=280,height=180)
        nwLabelFrame.pack()
        nwLabelFrame.propagate(False)

# east
class LabelFrameSampleE(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()
        self.pack()

    def create_widgets(self):
        nwLabelFrame  = ttk.LabelFrame(self,text="e-sample",labelanchor="e",width=280,height=180)
        nwLabelFrame.pack()
        nwLabelFrame.propagate(False)
# east-sorth
class LabelFrameSampleES(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()
        self.pack()

    def create_widgets(self):
        nwLabelFrame  = ttk.LabelFrame(self,text="es-sample",labelanchor="es",width=280,height=180)
        nwLabelFrame.pack()
        nwLabelFrame.propagate(False)
# sorth-east
class LabelFrameSampleSE(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()
        self.pack()

    def create_widgets(self):
        nwLabelFrame  = ttk.LabelFrame(self,text="se-sample",labelanchor="se",width=280,height=180)
        nwLabelFrame.pack()
        nwLabelFrame.propagate(False)
# sorth
class LabelFrameSampleS(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()
        self.pack()

    def create_widgets(self):
        nwLabelFrame  = ttk.LabelFrame(self,text="s-sample",labelanchor="s",width=280,height=180)
        nwLabelFrame.pack()
        nwLabelFrame.propagate(False)
# sorth-west
class LabelFrameSampleSW(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()
        self.pack()

    def create_widgets(self):
        nwLabelFrame  = ttk.LabelFrame(self,text="sw-sample",labelanchor="sw",width=280,height=180)
        nwLabelFrame.pack()
        nwLabelFrame.propagate(False)
# west-sorth
class LabelFrameSampleWS(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()
        self.pack()

    def create_widgets(self):
        nwLabelFrame  = ttk.LabelFrame(self,text="ws-sample",labelanchor="ws",width=280,height=180)
        nwLabelFrame.pack()
        nwLabelFrame.propagate(False)
# west
class LabelFrameSampleW(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()
        self.pack()

    def create_widgets(self):
        nwLabelFrame  = ttk.LabelFrame(self,text="w-sample",labelanchor="w",width=280,height=180)
        nwLabelFrame.pack()
        nwLabelFrame.propagate(False)
# west-north
class LabelFrameSampleWN(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()
        self.pack()

    def create_widgets(self):
        nwLabelFrame  = ttk.LabelFrame(self,text="wn-sample",labelanchor="wn",width=280,height=180)
        nwLabelFrame.pack()
        nwLabelFrame.propagate(False)



if __name__ == '__main__':
    master = Tk()
    master.title("LabelFrame-labelanchor")
    master.geometry("300x200")
    LabelFrameSampleNW(master)
    # LabelFrameSampleN(master)
    # LabelFrameSampleNE(master)
    # LabelFrameSampleEN(master)
    # LabelFrameSampleE(master)
    # LabelFrameSampleES(master)
    # LabelFrameSampleSE(master)
    # LabelFrameSampleS(master)
    # LabelFrameSampleSW(master)
    # LabelFrameSampleWS(master)
    # LabelFrameSampleW(master)
    # LabelFrameSampleWN(master)
    master.mainloop()
