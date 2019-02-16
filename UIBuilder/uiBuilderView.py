import tkinter.ttk as ttk
from tkinter import *


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


class WidgetsParts():
    """
    Widget群とCanvasFrameサイズを指定するパーツ
    """
    def __init__(self, parent):
        self.parent = parent
        self.width_var = None
        self.height_var = None
        self.command = None
        self.add_frame = None
        self.option_parts = None
        self.start_xy =None
        self.x_y=None
        self.createWidgets()

    def createWidgets(self):
        self.inputWHWidgets()
        self.inputWidgets()


    def inputWHWidgets(self):
        """
        widthとheightを入力する
        """

        option = {"width":"5"}
        frame = ttk.LabelFrame(self.parent,text="windowsize")
        frame.pack()
        input_frame = ttk.Frame(frame)
        input_frame.pack()
        width_parts = LabelEntryWidget(input_frame,text="width")
        width_parts.pack(side="left")
        width_parts.setEntryOption(option)
        height_parts = LabelEntryWidget(input_frame,text="height")
        height_parts.pack(side="left")
        height_parts.setEntryOption(option)

        self.update_button = ttk.Button(frame,text="update")
        self.update_button.pack()
        self.width_var = width_parts.getVar()
        self.height_var = height_parts.getVar()

    def getWidthVar(self):
        return self.width_var

    def getHeightVar(self):
        return self.height_var

    def setUpdateCommand(self,command):
        self.update_button["command"]  = command

    def inputWidgets(self):
        """
        Widget毎にボタンを作成
        commandには自身のクラスを引数にaddWidgetを登録
        """
        ttk.Button(self.parent,text= "Label",command = lambda : self.addWidget(ttk.Label)).pack()
        ttk.Button(self.parent,text= "Button",command = lambda : self.addWidget(ttk.Button)).pack()
        ttk.Button(self.parent,text= "Entry",command = lambda : self.addWidget(ttk.Entry)).pack()
        ttk.Button(self.parent,text= "CheckBox",command = lambda : self.addWidget(ttk.Checkbutton)).pack()
        ttk.Button(self.parent,text= "RadioButton",command = lambda : self.addWidget(ttk.Radiobutton)).pack()
        ttk.Button(self.parent,text= "ComboBox",command = lambda : self.addWidget(ttk.Combobox)).pack()

    def addWidget(self,widget):
        """
        widgetは作成するWidgetのクラス
        ボタン押下時にWidgetのクラスをオブジェクト化する
        """
        if self.add_frame is None:
            print("none")
            return
        widget = widget(self.add_frame)
        widget.place(x=50,y=50)
        if "text" in widget.keys():
            widget["text"] = "sample"
        widget.bind("<Button-1>",self.move_start)
        widget.bind("<B1-Motion>",self.move_now)
        widget.bind("<ButtonRelease-1>",self.move_end)


    def move_start(self,event):
        """
        Widgetが選択されたときの処理
        ①プロパティパーツの更新をする
        ②マウスカーソルの座標取得（スクリーン位置）
        ③位置情報取得（Canvas内の位置）
        """
        self.option_parts.make_child(event.widget)
        self.start_xy = (event.x_root,event.y_root)
        place_info = event.widget.place_info()
        x = int(place_info['x'])
        y = int(place_info['y'])
        self.x_y = (x,y)
        print(self.add_frame.winfo_reqwidth())


    def move_now(self,event):
        """
        移動中処理
        ①move_startで取得したマウスカーソル位置と現在のマウスカーソル位置で距離を計算
        ②計算した距離を対象のWidget位置に加算
        ③ｘ、ｙの移動後の座標を検査（Canvas内からはみ出る場合は調整）
        ④再配置
        """
        if self.start_xy is None:
            return
        # 移動距離を調べる
        distance = (event.x_root-self.start_xy[0],event.y_root-self.start_xy[1])
        # 再度座標を設定する
        place_info = event.widget.place_info()

        self.option_parts.setPlaceinfo(place_info)
        x = self.x_y[0] + distance[0]
        y = self.x_y[1] + distance[1]

        if x < 5:
            x = 5
        elif x >self.add_frame.winfo_reqwidth()-event.widget.winfo_reqwidth() - 10:
            x = self.add_frame.winfo_reqwidth()-event.widget.winfo_reqwidth() - 10
        if y < 5:
            y = 5
        elif y>self.add_frame.winfo_reqheight()-event.widget.winfo_reqheight() - 20:
            y = self.add_frame.winfo_reqheight()-event.widget.winfo_reqheight() - 20
        place_info['x'] = x
        place_info['y'] = y
        event.widget.place_configure(place_info)


    def move_end(self,event):
        """
        移動処理が終わったら座標類を初期化
        """
        self.start_xy = None
        self.x_y = None

    def setAddFrame(self,add_frame):
        self.add_frame = add_frame
        self.width_var.set(self.add_frame["width"])
        self.height_var.set(self.add_frame["height"])

    def setOptionParts(self,option_parts):
        self.option_parts = option_parts


class CanvasParts(ttk.Frame):
    """
    Widgetを配置するCanvas
    """
    def __init__(self, master,**kw):
        super().__init__(master,**kw)
        self.pack()

class OptionParts():
    """
    各Widgetのオプション値を編集するパーツ
    """
    def __init__(self, parent):
        self.parent = parent
        self.widget = None
        self.x = None
        self.y = None

    def make_child(self,widgets):
        """
        ①以前のパーツを削除
        ②与えられたWidgetによって編集可能なオプション値を探す。
        ③WidgetのCanvas内位置を変更する編集可能Widgetに座標を入力
        ④target_keyに当てはまるオプションの編集可能Widgetを作成
        """
        self.delete(destroy=False)
        self.widget = widgets
        target_key = ("width","height","text","state")
        option_dict={"width":"7"}
        itemdict = {}
        place_info = widgets.place_info()
        self.createWidgets()
        self.x.set(place_info['x'])
        self.y.set(place_info['y'])
        for key in widgets.keys():
            if key in target_key:
                label = LabelEntryWidget(self.parent,text=key)
                label.pack()
                label.setLabelOption(option_dict)
                itemdict[key] = label.getVar()
                itemdict[key].set(widgets[key])
        def _addCommand():
            """
            update用コマンド
            """
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
        """
        Widgetの座標位置を更新（マウスで動かされたときに同期する用）
        """
        self.x.set(place_info['x'])
        self.y.set(place_info['y'])

    def createWidgets(self):
        """
        操作（編集）対象のWidget共通項目
        Widgetの座標位置を編集するWidget
        """
        option_dict={"width":"7"}
        xlabel = LabelEntryWidget(self.parent,text="x")
        xlabel.pack()
        xlabel.setLabelOption(option_dict)
        self.x  = xlabel.getVar()
        ylabel = LabelEntryWidget(self.parent,text="y")
        ylabel.pack()
        ylabel.setLabelOption(option_dict)
        self.y  = ylabel.getVar()

    def delete(self,destroy=True):
        """
        現在編集対象Widgetの編集項目を削除する
        """
        children = self.parent.winfo_children()
        for child in children:
            child.destroy()
        if destroy:
            self.widget.destroy()



class UIBuilderApp(ttk.Frame):
    """
    各パーツを組み立てるメインView
    """
    def __init__(self, master):
        super().__init__(master)
        self.widgets_parts  = None
        self.canvs_parts = None
        self.option_parts = None
        self.output_command = lambda : print("none")
        self.setupMenu()
        self.createWidgets()
        self.pack()

    def createWidgets(self):
        widgets_frame  = ttk.Labelframe(self,text = "widgets",width="190",height="580")
        widgets_frame.propagate(False)
        widgets_frame.pack(side = "left")
        self.widgets_parts = widgetparts = WidgetsParts(widgets_frame)
        canvs_frame  = ttk.Labelframe(self,text = "canvas",width="400",height="580")
        canvs_frame.propagate(False)
        canvs_frame.pack(side = "left")
        self.canvs_parts = CanvasParts(canvs_frame,width="400",height="580")
        option_frame  = ttk.Labelframe(self,text = "option",width="190",height="580")
        option_frame.propagate(False)
        option_frame.pack(side = "left")
        self.option_parts = OptionParts(option_frame)
        self.widgets_parts.setAddFrame(self.canvs_parts)
        self.widgets_parts.setOptionParts(self.option_parts)
        self.setUpdateCommand()

    def getWidgetParts(self):
        return self.widgets_parts
    def getCsanvasParts(self):
        return self.canvs_parts

    def setUpdateCommand(self):

        def command():
            width = self.widgets_parts.getWidthVar().get()
            height = self.widgets_parts.getHeightVar().get()
            self.canvs_parts["width"] = width
            self.canvs_parts["height"] = height
            # 親のFrameもサイズを変更する
            parent = self.canvs_parts.master
            parent["width"] = width
            parent["height"] = height
        self.widgets_parts.setUpdateCommand(command)
    def setupMenu(self):

        menu = Menu(self.master)
        createMenu = Menu(menu,tearoff = 0)
        createMenu.add_command(label="output",command=lambda:self.output_command())
        exitMenu = Menu(menu,tearoff = 0)
        exitMenu.add_command(label="exit",command=lambda:self.master.destroy())
        menu.add_cascade(label="作成",menu = createMenu)
        menu.add_cascade(label="終了",menu = exitMenu)
        self.master.config(menu=menu)

    def getCanvasParts(self):
        """
        Canvasパーツを取得する
        """
        return self.canvs_parts

    def setOutputCommand(self,command):
        """
        ファイル出力コマンドの設定
        """
        print("set")
        self.output_command = command

if __name__ == '__main__':
    master = Tk()
    master.title("UIBuilder")
    master.geometry("800x600")
    UIBuilderApp(master)
    master.mainloop()
