from tkinter import *
import tkinter.ttk as ttk

class HelloWorldApp(ttk.Frame):

    def __init__(self, app):
        super().__init__(app)
        self.pack()
        label = ttk.Label(self,text="HelloWorld")
        label.pack()
        colorDict ={"red":"#ff0000",
                "green":"#00ff00",
                "blue":"#0000ff",
                "black":"#000000"}
        # 色ボタン作成
        self.ChangeColorButtonDictVer(colorDict,label)

    #色ボタン作成
    def ChangeColorButton(self,buttonname,color,label):
        button = ttk.Button(self,text= buttonname, command=lambda:self.changeColor(label,color))
        button.pack()
    #辞書に登録された色の数だけボタン作成
    def ChangeColorButtonDictVer(self,dict,label):
        keys = dict.keys()
        for key in keys:
            color  = dict.get(key)
            self.ChangeColorButton(key,color,label)

    # targetLabelの文字色をcolorに変更する
    def changeColor(self,targetLabel,color):
        targetLabel["foreground"]=color

if __name__ == '__main__':
    #Tkインスタンスを作成し、app変数に格納する
    app  = Tk()
    #縦幅400横幅300に画面サイズを変更します。
    app.geometry("400x300")
    #タイトルを指定
    app.title("Hello World Program")
    # #フレームを作成する
    frame = HelloWorldApp(app)
    # 格納したTkインスタンスのmainloopで画面を起こす
    app.mainloop()
