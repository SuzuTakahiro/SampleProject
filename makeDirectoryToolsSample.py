import os
from tkinter import *
import tkinter.ttk as ttk
import tkinter.filedialog as filedialog
import os

class Directory():

    # subDirs -> Directory List
    def __init__(self, dirPath,subDirs=None):
        self.dirPath = dirPath
        self.subDirs = subDirs

    def getDirs(self):
        return self.subDirs

    def getDirPath(self):
        return self.dirPath

class MakeDirectoryLogic():
    def __init__(self,rootPath,selectNode):
        self.rootPath = rootPath
        self.selectNode = selectNode


    def openFileDialog(self):
        file  = filedialog.askdirectory();
        self.rootPath.set(file)


    def makeDirectory(self,rootPath,dirList):
        if os.path.exists(rootPath) ==False:
            return
        for dir in dirList:
            path = os.path.join(rootPath,dir.getDirPath())
            print("path",path)
            os.mkdir(path)
            children = dir.getDirs()
            if len(children) > 0:
                self.makeDirectory(path,children)

    def createDirectoryList(self,rootiid,tree,dirList):
        dirname = tree.item(rootiid,"text")
        print(dirname)
        children = tree.get_children(rootiid)
        childlist=[]
        dir = Directory(dirname,childlist)
        dirList.append(dir)
        if len(children)>0:
            for child in children:
                self.createDirectoryList(child,tree,childlist)
    def act(self,tree):
        dirList=[]
        self.createDirectoryList("I001",tree,dirList)
        print(len(dirList[0].getDirs()))
        self.makeDirectory(self.rootPath.get(),dirList)


class MakeDirectoryTools(ttk.Frame):

    def __init__(self,master):
        super().__init__(master)

        self.rootPath = StringVar()
        self.addNode = StringVar()
        self.selectNode = StringVar()
        self.iid=""
        self.logic = MakeDirectoryLogic(self.rootPath,self.iid)
        self.create_widgets()

    def create_widgets(self):
        leftframe = self.createTreeView()
        leftframe.pack(side="left")
        rightframe= self.createInputPanel()
        rightframe.pack(side="right")
        self.pack()

    def createTreeView(self):
        treeFrame = ttk.Frame(self)
        self.tree = ttk.Treeview(treeFrame)
        self.tree.bind("<<TreeviewSelect>>",self.selectNodeFunc)
        self.tree.pack()
        # rootを登録
        self.iid = self.tree.insert("","end",text="makedirectoryTools")
        return treeFrame

    def createInputPanel(self):
        inputFrame = ttk.LabelFrame(self,text="InputParam",height=200)
        inputFrame.propagate(False)
        # rootPathFrame = ttk.Frame(inputFrame)
        # rootPathFrame.pack()

        rootPathLabel = ttk.Label(inputFrame,text="RootPath")
        rootPathLabel.grid(column=0,row=0)
        rootpathEntry = ttk.Entry(inputFrame,textvariable=self.rootPath)
        rootpathEntry.grid(column=1,row=0)
        rootpathButton = ttk.Button(inputFrame,text="open",command=self.logic.openFileDialog)
        rootpathButton.grid(column=2,row=0)

        addPathLabel = ttk.Label(inputFrame,text="SelectDir")
        addPathLabel.grid(column=0,row=1)
        addpathEntry = ttk.Entry(inputFrame,state="readonly",textvariable=self.selectNode)
        addpathEntry.grid(column=1,row=1)
        addPathButton = ttk.Button(inputFrame,text="delete")
        addPathButton.grid(column=2,row=1)


        addNodeLabel = ttk.Label(inputFrame,text="AddDir")
        addNodeLabel.grid(column=0,row=2)
        addNodeEntry = ttk.Entry(inputFrame,textvariable=self.addNode)
        addNodeEntry.grid(column=1,row=2)
        addNodeButton = ttk.Button(inputFrame,text="add",command=self.insertNode)
        addNodeButton.grid(column=2,row=2)

        makeDirButton = ttk.Button(inputFrame,text="makeDirectory",command=lambda:self.logic.act(self.tree))
        makeDirButton.grid(column=2,row=3)



        return inputFrame
    def insertNode(self):
        if self.addNode.get() is not "":
            self.tree.insert(self.iid,"end",text=self.addNode.get())
        pass
    def selectNodeFunc(self,event):
        self.iid = self.tree.focus()
        if self.iid :
            self.selectNode.set(self.tree.item(self.iid,"text"))







if __name__ == '__main__':
    master = Tk()
    master.title("MakeDirectory Tools")
    dir = MakeDirectoryTools(master)

    master.mainloop()
