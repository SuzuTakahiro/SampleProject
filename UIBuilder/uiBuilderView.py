import tkinter.ttk as ttk
from tkinter import *

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

# Widget群とCanvasFrameサイズを指定するパーツ
class WidgetsParts():
    def __init__(self, parent):
        self.parent = parent
        self.widthVar = None
        self.heightVar = None
        self.command = None
        self.addFrame = None
        self.optionParts= None
        self.start_xy =None
        self.x_y=None
        self.createWidgets()

    def createWidgets(self):
        self.inputWHWidgets()
        self.inputWidgets()
        # self.inputTemplateWidgets()
    # widthとheightを入力する
    def inputWHWidgets(self):
        option = {"width":"5"}
        frame = ttk.LabelFrame(self.parent,text="windowsize")
        frame.pack()
        inputframe = ttk.Frame(frame)
        inputframe.pack()
        widthparts = LabelEntryWidget(inputframe,text="width")
        widthparts.pack(side="left")
        widthparts.setEntryOption(option)
        heightparts = LabelEntryWidget(inputframe,text="height")
        heightparts.pack(side="left")
        heightparts.setEntryOption(option)

        self.updateButton = ttk.Button(frame,text="update")
        self.updateButton.pack()
        self.widthVar = widthparts.getVar()
        self.heightVar = heightparts.getVar()

    def getWidthVar(self):
        return self.widthVar

    def getHeightVar(self):
        return self.heightVar

    def setUpdateCommand(self,command):
        self.updateButton["command"]  = command

    def inputWidgets(self):
        ttk.Button(self.parent,text= "Label",command = lambda : self.addWidget(ttk.Label)).pack()
        ttk.Button(self.parent,text= "Button",command = lambda : self.addWidget(ttk.Button)).pack()
        ttk.Button(self.parent,text= "Entry",command = lambda : self.addWidget(ttk.Entry)).pack()
        ttk.Button(self.parent,text= "CheckBox",command = lambda : self.addWidget(ttk.Checkbutton)).pack()
        ttk.Button(self.parent,text= "RadioButton",command = lambda : self.addWidget(ttk.Radiobutton)).pack()
        ttk.Button(self.parent,text= "ComboBox",command = lambda : self.addWidget(ttk.Combobox)).pack()

    def addWidget(self,widget):
        if self.addFrame is None:
            print("none")
            return
        widget = widget(self.addFrame)
        widget.place(x=50,y=50)
        if "text" in widget.keys():
            widget["text"] = "sample"
        widget.bind("<Button-1>",self.move_start)
        widget.bind("<B1-Motion>",self.move_now)
        widget.bind("<ButtonRelease-1>",self.move_end)

    # Widgetが選択されたときの処理
    def move_start(self,event):
        # プロパティパーツの更新をする

        self.optionParts.make_child(event.widget)
        # マウスカーソルの座標取得
        self.start_xy = (event.x_root,event.y_root)

        # 位置情報取得
        place_info = event.widget.place_info()
        x = int(place_info['x'])
        y = int(place_info['y'])
        self.x_y = (x,y)
        print(self.addFrame.winfo_reqwidth())

    # 移動中処理
    def move_now(self,event):
        if self.start_xy is None:
            return
        # 移動距離を調べる
        distance = (event.x_root-self.start_xy[0],event.y_root-self.start_xy[1])
        # 再度座標を設定する
        place_info = event.widget.place_info()

        self.optionParts.setPlaceinfo(place_info)
        x = self.x_y[0] + distance[0]
        y = self.x_y[1] + distance[1]

        if x < 5:
            x = 5
        elif x >self.addFrame.winfo_reqwidth()-event.widget.winfo_reqwidth()-10:
            x = self.addFrame.winfo_reqwidth()-event.widget.winfo_reqwidth()-10
        if y<5:
            y=5
        elif y>self.addFrame.winfo_reqheight()-event.widget.winfo_reqheight()-20:
            y = self.addFrame.winfo_reqheight()-event.widget.winfo_reqheight()-20
        place_info['x'] = x
        place_info['y'] = y
        event.widget.place_configure(place_info)

    # 移動処理が終わったら座標類を初期化
    def move_end(self,event):

        self.start_xy = None
        self.x_y = None
    #
    def setAddFrame(self,addFrame):
        self.addFrame = addFrame
        self.widthVar.set(self.addFrame["width"])
        self.heightVar.set(self.addFrame["height"])

    def setOptionParts(self,optionParts):
        self.optionParts = optionParts





class CanvasParts(ttk.Frame):

    def __init__(self, master,**kw):
        super().__init__(master,**kw)
        self.pack()
class OptionParts():

    def __init__(self, parent):
        self.parent = parent
        self.widget = None
        self.x = None
        self.y = None

    def make_child(self,widgets):
        self.delete(destroy=False)
        self.widget = widgets
        targetkey = ("width","height","text","state")
        optiondict={"width":"7"}
        itemdict = {}
        place_info = widgets.place_info()
        self.createWidgets()
        self.x.set(place_info['x'])
        self.y.set(place_info['y'])
        for key in widgets.keys():
            if key in targetkey:
                label = LabelEntryWidget(self.parent,text=key)
                label.pack()
                label.setLabelOption(optiondict)
                itemdict[key] = label.getVar()
                itemdict[key].set(widgets[key])
        def _addCommand():
            for item in itemdict.keys():
                widgets[item] = itemdict[item].get()
            place_info['x']=self.x.get()
            place_info['y']=self.y.get()
            widgets.place_configure(place_info)

        update = ttk.Button(self.parent,text = "update",command = _addCommand)
        update.pack()
        delete = ttk.Button(self.parent,text = "destroy",command = self.delete)
        delete.pack()

    def setPlaceinfo(self,place_info):
        self.x.set(place_info['x'])
        self.y.set(place_info['y'])

    def createWidgets(self):

        optiondict={"width":"7"}
        xlabel = LabelEntryWidget(self.parent,text="x")
        xlabel.pack()
        xlabel.setLabelOption(optiondict)
        self.x  = xlabel.getVar()
        ylabel = LabelEntryWidget(self.parent,text="y")
        ylabel.pack()
        ylabel.setLabelOption(optiondict)
        self.y  = ylabel.getVar()

    def delete(self,destroy=True):
        children = self.parent.winfo_children()
        for child in children:
            child.destroy()
        if destroy:
            self.widget.destroy()



class UIBuilderApp(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.widgetsParts  = None
        self.canvsParts = None
        self.optionParts = None
        self.outputCommand = lambda : print("none")
        self.setupMenu()
        self.createWidgets()
        self.pack()

    def createWidgets(self):
        widgetsFrame  = ttk.Labelframe(self,text = "widgets",width="190",height="580")
        widgetsFrame.propagate(False)
        widgetsFrame.pack(side = "left")
        self.widgetsParts = widgetparts = WidgetsParts(widgetsFrame)
        canvsFrame  = ttk.Labelframe(self,text = "canvas",width="400",height="580")
        canvsFrame.propagate(False)
        canvsFrame.pack(side = "left")
        self.canvsParts = CanvasParts(canvsFrame,width="400",height="580")
        optionFrame  = ttk.Labelframe(self,text = "option",width="190",height="580")
        optionFrame.propagate(False)
        optionFrame.pack(side = "left")
        self.optionParts = OptionParts(optionFrame)
        self.widgetsParts.setAddFrame(self.canvsParts)
        self.widgetsParts.setOptionParts(self.optionParts)
        self.setUpdateCommand()

    def getWidgetParts(self):
        return self.widgetsParts
    def getCsanvasParts(self):
        return self.canvsParts

    def setUpdateCommand(self):

        def command():
            width = self.widgetsParts.getWidthVar().get()
            height = self.widgetsParts.getHeightVar().get()
            self.canvsParts["width"]=width
            self.canvsParts["height"]=height
            # 親のFrameもサイズを変更する
            parent = self.canvsParts.master
            parent["width"]=width
            parent["height"]=height
        self.widgetsParts.setUpdateCommand(command)
    def setupMenu(self):

        menu = Menu(self.master)
        createMenu = Menu(menu,tearoff = 0)
        createMenu.add_command(label="output",command=lambda:self.outputCommand())
        exitMenu = Menu(menu,tearoff = 0)
        exitMenu.add_command(label="exit",command=lambda:self.master.destroy())
        menu.add_cascade(label="作成",menu = createMenu)
        menu.add_cascade(label="終了",menu = exitMenu)
        self.master.config(menu=menu)
    # Canvasパーツを取得する
    def getCanvasParts(self):
        return self.canvsParts
    #ファイル出力コマンドの設定
    def setOutputCommand(self,command):
        print("set")
        self.outputCommand = command
        # self.outputCommand()




if __name__ == '__main__':
    master = Tk()
    master.title("UIBuilder")
    master.geometry("800x600")
    UIBuilderApp(master)
    master.mainloop()
