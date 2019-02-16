import tkinter.ttk as ttk
from tkinter import *
from uiBuilderView import UIBuilderApp
import os
import tkinter.messagebox as messagebox

class UIBuilderLogic():
    """
    UIBuilderで組み立てたUIのサンプルコードを出力するロジッククラス
    """
    def __init__(self,canvas_parts):
        """
        初期化
        出力ディレクトリはこのファイルと同じ階層
        出力ファイル名はtest.pyとして出力する
        canvas_parts:パーツを配置した親フレーム
        """
        self.output_dir = os.path.dirname(__file__)
        self.output_file_name = os.path.join(self.output_dir,"test.py")
        self.canvas_parts = canvas_parts

    def outputCommand(self):
        """
        実際に出力させるメインメソッド
        ①インポート文出力
        ②UISampleクラス出力
        ③main文出力
        """
        ret = False
        try:
            fo = open(self.output_file_name,"w",newline= "\n")
            self.writeImport(fo)
            self.writeUISample(fo)
            self.writeMain(fo)
            fo.close()
            ret = True
        except IOError as e:
            print(e)
            print("ファイルの出力に失敗しました。")
            ret = False
        return ret

    def writeImport(self,file):
        """
        import文の出力
        file:ファイルオブジェクト
        """
        import_list =[
        "import tkinter.ttk as ttk",
        "from tkinter import *",
        ]
        for item in import_list:
            print(item,file=file)

    def writeUISample(self,file):
        """
        実際のWidget作成
        UISampleクラスを作成しCanvasに配置したWidgetを組み立てる
        フレームサイズは指定サイズで作成
        file:ファイルオブジェクト
        """
        width = self.canvas_parts["width"]
        height = self.canvas_parts["height"]
        print("class UISample(ttk.Frame):",file=file)
        print("\tdef __init__(self, master):",file=file)
        print("\t\tsuper().__init__(master,width='{}',height='{}')".format(width,height),file=file)
        print("\t\tself.createWidgets()",file=file)
        print("\t\tself.propagate(False)",file=file)
        print("\t\tself.pack()",file=file)
        print("\tdef createWidgets(self):",file=file)
        child_idx = 0
        button_command = []
        for child in self.canvas_parts.winfo_children():
            place_info = child.place_info()
            x = place_info['x']
            y = place_info['y']
            class_name = child.__class__.__name__

            option = ""
            target_key = ("width","height","text","state","command")
            for ck in child.keys():
                if ck in target_key:
                    if ck == "command":
                        command_function = "self.commandFunction{}".format(child_idx)
                        button_command.append(command_function)
                        option = option + "{} = {},".format(ck,command_function)
                    else:
                        option  =option + "{} = \"{}\",".format(ck,child[ck])
            print("\t\twidget_{} = ttk.{}(self,{})".format(child_idx,class_name,option),file=file)
            print("\t\twidget_{}.place(x={},y={})".format(child_idx,x,y),file=file)
            child_idx +=1
        self.writeCommandFunction(file,button_command)

    def writeCommandFunction(self,file,command_list):
        """
        ボタンコマンドを作成する
        とりあえずなにもしないpass文を書いておく
        command_list:ボタンの関数リスト
        """
        for command in command_list:
            func_name =  command.replace("self.","")
            print("\tdef {}(self):".format(func_name),file=file)
            print("\t\tpass",file=file)

    def writeMain(self,file):
        """
        main文の作成
        file:ファイルオブジェクト
        """
        width = self.canvas_parts["width"]
        height = self.canvas_parts["height"]
        main_list=[
        "if __name__ == '__main__':",
        "\tmaster = Tk()",
        "\tmaster.title('UISample')",
        "\tmaster.geometry(\"{}x{}\")".format(width,height),
        "\tUISample(master)",
        "\tmaster.mainloop()"
        ]
        for item in main_list:
            print(item,file=file)


class UIBuilderControl():
    """
    UIBuilderのViewとLogicの管理を行うコントロール
    """
    def __init__(self):
        """
        UIBilderの起動を行う
        """
        master = Tk()
        master.title("UIBuilder")
        master.geometry("800x600")
        self.view =view= UIBuilderApp(master)
        self.logic = UIBuilderLogic(view.getCanvasParts())
        self.setupMenu()
        master.mainloop()
    def setupMenu(self):
        """
        作成メニューのoutputにsetOutputCommandを紐づける
        """
        self.view.setOutputCommand(self.setOutputCommand)

    def setOutputCommand(self):
        """
        ロジックの出力メソッドを実行する
        実行結果によってメッセージボックスを切り替え
        """
        ret = self.logic.outputCommand()
        if ret:
            messagebox.showinfo("output", "succeed")
        else:
            messagebox.showerror("output", "failed")


if __name__ == '__main__':
    UIBuilderControl()
