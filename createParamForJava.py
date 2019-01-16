from tkinter import *
import tkinter.ttk as ttk
import tkinter.filedialog as filedialog
import tkinter.messagebox as messagebox
import os

class CreateParamToolsLogic():
    def __init__(self):
        self.outfolder = os.path.dirname(__file__)
        self.outFileName=""

    def mkFileForJava(self,outfolder,paramlist):
        self.outFileName="createparamforJava.out"

        if(os.path.exists(outfolder) and os.path.isdir(outfolder)):
            self.outfolder= outfolder
        else:
            self.outfolder = os.path.dirname(__file__)
        path = os.path.join(self.outfolder,self.outFileName)
        print(path)
        variables=[]
        setterList = []
        getterList =[]
        for param in paramlist :
            className = param[0]
            variableName = param[1]
            value = param[2]
            variable = "private "+className+" "+variableName+" = "+value+";"
            func = variableName[0].upper()+variableName[1:]
            setter = "public void set"+func+"("+className+" "+variableName+"){\n"+"\tthis."+variableName+" = "+ variableName+ ";\n}"
            getter = "public "+className+" get"+func+"(){\n"+"\treturn this."+variableName+";\n}"
            variables.append(variable)
            setterList.append(setter)
            getterList.append(getter)
        file = open(path,"w",newline="\n")
        print(path)
        for var in variables:
            print(var,file=file)
        for setter in setterList:
            print(setter,file=file)
        for getter in getterList:
            print(getter,file=file)
        file.close()


# 変数パラメータ入力用パネル
class InputVariable(ttk.Frame):
    def __init__(self,master,id=1):
        super().__init__(master)
        self.className = StringVar()
        self.variableName = StringVar()
        self.value = StringVar()
        self.classValues=["int","double","float","String"]
        self.create_widgets(id)


    def create_widgets(self,id):
        indexLabel = ttk.Label(self,text="id:"+str(id))
        indexLabel.pack(side="left")
        classNameLabel = ttk.Label(self,text="型")
        classNameLabel.pack(side="left")
        classNameCombo = ttk.Combobox(self,text="型",values=self.classValues,textvariable=self.className)
        classNameCombo.pack(side="left")
        variableNameLabel = ttk.Label(self,text="変数名")
        variableNameLabel.pack(side="left")
        variableNameEntry = ttk.Entry(self,textvariable =self.variableName)
        variableNameEntry.pack(side="left")
        valueLabel = ttk.Label(self,text="初期値")
        valueLabel.pack(side="left")
        valueEntry = ttk.Entry(self,textvariable =self.value)
        valueEntry.pack(side="left")

    def getClassName(self):
        return self.className.get()

    def getVariableName(self):
        return self.variableName.get()

    def getValue(self):
        return self.value.get()

class CreateParamTools(ttk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.pack()
        self.outfolder=StringVar()
        self.create_widgets()
        self.inputVariableList=[]
        self.logic = CreateParamToolsLogic()

    def create_widgets(self):
        topFrame = ttk.Frame(self)
        topFrame.pack()
        folderLabel = ttk.Label(topFrame,text="フォルダ")
        folderLabel.pack(side="left")
        folderEntry = ttk.Entry(topFrame,textvariable=self.outfolder,exportselection=True)
        folderEntry.pack(side="left")
        openButton = ttk.Button(topFrame,text="open",command=self.openDirectory)
        openButton.pack(side="left")
        addVarButton = ttk.Button(topFrame,text="addVar",command=self.addVariable)
        addVarButton.pack(side="left")
        mkFileButton = ttk.Button(topFrame,text="mkFile",command=self.mkFile)
        mkFileButton.pack(side="left")

    def addVariable(self):
        index= len(self.inputVariableList) + 1
        inputVariable = InputVariable(self,index)
        inputVariable.pack()
        self.inputVariableList.append(inputVariable)

    def openDirectory(self):
        dir = filedialog.askdirectory()
        self.outfolder.set(dir)
    def mkFile(self):
        paramlist =[]
        for widget in self.inputVariableList:
            if widget.getVariableName !="" :
                param=[widget.getClassName(),widget.getVariableName(),widget.getValue()]
                paramlist.append(param)
        self.logic.mkFileForJava(self.outfolder.get(),paramlist)


if __name__ == '__main__':
    master = Tk()
    master.geometry("600x400")
    master.title("CreateParamToolsForJava")
    CreateParamTools(master)
    master.mainloop()
