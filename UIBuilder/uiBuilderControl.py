import tkinter.ttk as ttk
from tkinter import *
from uiBuilderView import UIBuilderApp
import os

class UIBuilderLogic():
    """docstring for ."""
    def __init__(self,canvasParts):
        self.outputDir = os.path.dirname(__file__)
        self.outputFileName = os.path.join(self.outputDir,"test.py")
        self.canvasParts = canvasParts

    def outputCommand(self):
        print("output")
        fo = open(self.outputFileName,"w",newline= "\n")
        self.writeimport(fo)
        self.writeUISample(fo)
        self.writemain(fo)

        fo.close()
    def writeimport(self,file):
        importList =[
        "import tkinter.ttk as ttk",
        "from tkinter import *",
        ]
        for item in importList:
            print(item,file=file)
    def writeUISample(self,file):
        width = self.canvasParts["width"]
        height = self.canvasParts["height"]
        print("class UISample(ttk.Frame):",file=file)
        print("\tdef __init__(self, master):",file=file)
        print("\t\tsuper().__init__(master,width='{}',height='{}')".format(width,height),file=file)
        print("\t\tself.createWidgets()",file=file)
        print("\t\tself.propagate(False)",file=file)
        print("\t\tself.pack()",file=file)
        print("\tdef createWidgets(self):",file=file)
        childidx = 0
        for child in self.canvasParts.winfo_children():
            pinfo = child.place_info()
            x =pinfo['x']
            y =pinfo['y']
            classname = child.__class__.__name__

            option = ""
            targetkey = ("width","height","text","state")
            for ck in child.keys():
                if ck in targetkey:
                    option =option+"{} = \"{}\",".format(ck,child[ck])
            print("\t\twidget{} = ttk.{}(self,{})".format(childidx,classname,option),file=file)
            print("\t\twidget{}.place(x={},y={})".format(childidx,x,y),file=file)
            childidx +=1

    def writemain(self,file):
        width = self.canvasParts["width"]
        height = self.canvasParts["height"]
        mainList=[
        "if __name__ == '__main__':",
        "\tmaster = Tk()",
        "\tmaster.title('UISample')",
        "\tmaster.geometry(\"{}x{}\")".format(width,height),
        "\tUISample(master)",
        "\tmaster.mainloop()"
        ]
        for item in mainList:
            print(item,file=file)
        # def setCanvasParts(self,canvasParts):
        #     self.canvsParts = canvasParts


class UIBuilderControl():
    def __init__(self):
        master = Tk()
        master.title("UIBuilder")
        master.geometry("800x600")
        self.view =view= UIBuilderApp(master)
        self.logic = UIBuilderLogic(view.getCanvasParts())

        self.setupMenu()
        master.mainloop()
    def setupMenu(self):
        self.view.setOutputCommand(self.logic.outputCommand)


if __name__ == '__main__':
    UIBuilderControl()
