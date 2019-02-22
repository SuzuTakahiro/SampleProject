from tkinter import *
import tkinter.ttk as ttk
import tkinter.filedialog as filedialog

class FileOpenFrame(ttk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.filePath = StringVar()
        self.createWidget()
        self.pack()

    def createWidget(self):
        filePathLabel = ttk.Label(self,text="FilePath")
        filePathLabel.grid(column=0,row=0)
        filepathEntry = ttk.Entry(self,textvariable=self.filePath)
        filepathEntry.grid(column=1,row=0)
        filepathButton = ttk.Button(self,text="open",command=self.openFileDialog)
        filepathButton.grid(column=2,row=0)
    def openFileDialog(self):
        file  = filedialog.askopenfilename(filetypes=[("csv", "*.csv")]);
        self.filePath.set(file)

class TreeView(ttk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.tree = None
        self.selected_iid = None
        self.columns =[]
        self.createWidget()
        self.pack()
        self.setTestData()
    def createWidget(self):
        self.tree = ttk.Treeview(self)
        self.tree["show"] = "headings"
        self.tree.pack()

    def setColomns(self,columns):
        self.columns = columns
        self.tree["columns"] = self.columns
        for col in columns:
            self.tree.heading(col,text=col)

    def setRow(self,index ="" ,row_data=[]):
        self.tree.insert("",index="end",text=index,values = row_data)

    def setRows(self,rows_data):
        for i,row_data in enumerate(rows_data):
            self.setRow(index = i,row_data = row_data)

    def setTestData(self):
        column_data = ("Name","Num","Value")
        rows_data = [("orange",3,120),("Apple",2,180)]
        self.deleteRows()
        self.setColomns(column_data)
        self.setRows(rows_data)

    def setTestData2(self):
        column_data = ("Name","Num","Value","Stock")
        rows_data = [("orange",3,120,10),("Apple",2,180,200)]
        self.deleteRows()
        self.setColomns(column_data)
        self.setRows(rows_data)

    def deleteRows(self):
        children = self.tree.get_children("")
        for child in children:
            self.tree.delete(child)
    def addSelectAction(self,func):
        self.tree.bind("<<TreeviewSelect>>",func)
    def getItem(self):
        self.selcted_iid = self.tree.focus()
        return self.tree.item(self.selcted_iid,"values")
    def getColumn(self):
        return self.columns

    def getDataMap(self):
        item = self.getItem()
        if len(self.columns) != len(item):
            return {"none":"none"}
        else:
            data_map = {}
            for i,column in enumerate(self.columns):
                data_map[column] = item[i]
            return data_map
    def updateValue(self,iid,new_values):
        self.tree.item(self.iid,values=new_values)
    def updateValue(self,new_values):
        self.tree.item(self.selcted_iid,values=new_values)
    def update(self,value):
        data =[]
        for column in self.columns:
            data.append(value[column])
        self.updateValue(data)
    def insert(self,value):
        data =[]
        for column in self.columns:
            data.append(value[column])
        print(data)
        children = self.tree.get_children("")
        index = len(children)
        self.setRow(index = str(index), row_data=data)

class LabelEntryWidget(ttk.Frame):
    """
    LabelとEntryがくっついたWidget
    """
    def __init__(self, master,text="property"):
        super().__init__(master)
        self.value = StringVar()
        self.createWidgets(text)

    def createWidgets(self,text="property"):
        self.label = ttk.Label(self,text=text)
        self.label.pack(side="left")
        self.entry = ttk.Entry(self,textvariable=self.value)
        self.entry.pack(side="left")

    def getVar(self):
        """
        値を取得するためのWidget変数の取得
        """
        return self.value


    def setLabelOption(self,key_dict):
        """
        Labelのオプション指定(オプションはdictで渡す)
        """
        for k in key_dict.keys():
            self.label[k] = key_dict[k]


    def setEntryOption(self,key_dict):
        """
        Entryのオプション指定(オプションはdictで渡す)
        """
        for k in key_dict.keys():
            self.entry[k] = key_dict[k]


class PropertyView(ttk.Frame):

    def __init__(self,master):
        super().__init__(master)
        self.pack()
        self.param_dict={}

    def createWidget(self,columns):
        self.delete()

        for column in columns:
            option = {"width":10}
            param = LabelEntryWidget(self,text = column)
            param.setLabelOption(option)
            param.pack()
            self.param_dict[column] = param.getVar()
        self.update_button = update = ttk.Button(self,text = "commit")
        self.insert_button = insert = ttk.Button(self,text = "insert")
        update.pack()
        insert.pack()


    def delete(self):
        children = self.winfo_children()
        for child in children:
            child.destroy()

    def setUpdateButtonCommand(self,command):
        self.update_button["command"] = command

    def setInsertButtonCommand(self,command):
        self.insert_button["command"] = command

    def setParameter(self,param):
        for key in self.param_dict.keys():
            self.param_dict[key].set(param[key])

    def getParameter(self):
        param_dict = {}
        for key,value in self.param_dict.items():
            param_dict[key] = value.get()
        return param_dict


class CSVView(ttk.Frame):
    """docstring for ."""
    def __init__(self, master):
        super().__init__(master)
        self.tree = None
        self.createWidget()
        self.setAction()
        self.pack()
    def createWidget(self):
        left_frame = ttk.LabelFrame(self,text="DB")
        left_frame.pack(side="left")
        self.tree = TreeView(left_frame)
        right_frame = ttk.LabelFrame(self,text="param")
        right_frame.pack(side = "right")
        # FileOpenFrame(right_frame)
        self.property  =PropertyView(right_frame)
        self.property.createWidget(self.tree.getColumn())

    def setAction(self):
        def _updateCommand():
            param = self.property.getParameter()
            print(param)
            self.tree.update(param)
        def _insertCommand():
            param = self.property.getParameter()
            self.tree.insert(param)

        def _func(event):
            self.property.setParameter(self.tree.getDataMap())

            self.property.setUpdateButtonCommand(_updateCommand)
            self.property.setInsertButtonCommand(_insertCommand)

        self.tree.addSelectAction(_func)








if __name__ == '__main__':
    master = Tk()
    master.title("csvview")
    CSVView(master)
    master.geometry("800x400")
    master.mainloop()
