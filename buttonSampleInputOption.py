from tkinter import *
import tkinter.ttk as ttk

# LabelとEntryがくっついたWidget
class LabelEntryWidget(ttk.Frame):
    def __init__(self, master,text="property"):
        super().__init__(master)
        self.value = StringVar()
        self.createWidgets(text)

    def createWidgets(self,text="property"):
        self.label = ttk.Label(self,text=text)
        self.label.pack(side="left")
        self.entry = ttk.Entry(self,textvariable=self.value)
        self.entry.pack(side="left")
    # 値を取得するためのWidget変数の取得
    def getVar(self):
        return self.value

    #Labelのオプション指定(オプションはdictで渡す)
    def setLabelOption(self,keydict):
        for k in keydict.keys():
            self.label[k] = keydict[k]
    #Entryのオプション指定(オプションはdictで渡す)
    def setEntryOption(self,keydict):
        for k in keydict.keys():
            self.entry[k] = keydict[k]





class ButtonSampleInputOption(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.createWidgets()
        self.pack()

    def createWidgets(self):
        buttonFrame = ttk.Frame(self,width = "200",height = "200")
        buttonFrame.propagate(False)
        buttonFrame.pack(side="left")
        self.button = ttk.Button(buttonFrame,text = "button")
        self.button.place(x = "50",y = "100")

        propertyFrame = ttk.LabelFrame(self,text ="property",width = "200",height = "200")
        propertyFrame.propagate(False)
        propertyFrame.pack(side="left")
        self.createPropertyWidgets(propertyFrame)
    # プロパティフレーム用のWidget作成を行う
    def createPropertyWidgets(self,frame):

        prop = {}
        #ラベルの幅を統一する
        labelOption = {"width":"7"}

        #ボタンの幅オプション用入力
        prop1 = LabelEntryWidget(frame,text="width")
        prop1.pack()
        prop1.setLabelOption(labelOption)
        # LabelEntryWidgetのEntryに紐づいたWidget変数を取得する
        p1Var = prop1.getVar()
        p1Var.set(self.button["width"])

        #ボタンのテキストオプション用入力
        prop2 = LabelEntryWidget(frame,text="text")
        prop2.pack()
        prop2.setLabelOption(labelOption)
        # LabelEntryWidgetのEntryに紐づいたWidget変数を取得する
        p2Var = prop2.getVar()
        p2Var.set(self.button["text"])

        # dictでオプション名と入力値をもったWidget変数を紐づける
        prop["width"] = p1Var
        prop["text"] = p2Var

        # 更新ボタン
        updateButton= ttk.Button(frame,text ="update",command = lambda :self.updateCommand(prop))
        updateButton.pack()

    #ボタンのオプションの値を更新する
    def updateCommand(self,propdict):
        for key in propdict.keys():
            # propdictとキーは共通だが、Widget変数が入っているので値はget()で取得
            self.button[key] = propdict[key].get()






if __name__ == '__main__':
    master = Tk()
    master.title("ButtonSampleInputOption")
    master.geometry("420x220")
    ButtonSampleInputOption(master)
    master.mainloop()
