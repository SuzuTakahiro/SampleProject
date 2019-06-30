from tkinter import *
import tkinter.ttk as ttk

#アプリケーションを終了する　applicationにはTKのインスタンスを指定する
def exit(application):
    application.destroy()

# ラベルの色を変更する 各オプションには[オプション]でアクセスする　colorは16進数表記
def changeColor(targetLabel,color):
    targetLabel["foreground"]=color



if __name__ == '__main__':
    #Tkインスタンスを作成し、app変数に格納する
    app  = Tk()
    #縦幅400横幅300に画面サイズを変更します。
    app.geometry("400x300")
    #タイトルを指定
    app.title("Hello World Program")
    #フレームを作成する
    frame = ttk.Frame(app)
    frame.pack()
    #ラベル作成
    label = ttk.Label(frame,text="Hello World")
    label.pack()
    #ボタン作成
    exitButton = ttk.Button(frame,text="exit",command=lambda:exit(app))
    exitButton.pack()
    #赤色に変更
    redButton = ttk.Button(frame,text="red",command=lambda:changeColor(label,"#ff0000"))
    redButton.pack()
    #緑色に変更
    greenButton = ttk.Button(frame,text="green",command=lambda:changeColor(label,"#00ff00"))
    greenButton.pack()
    #青色に変更
    blueButton = ttk.Button(frame,text="blue",command=lambda:changeColor(label,"#0000ff"))
    blueButton.pack()
    #黒色に変更
    blackButton = ttk.Button(frame,text="black",command=lambda:changeColor(label,"#000000"))
    blackButton.pack()
    #格納したTkインスタンスのmainloopで画面を起こす
    app.mainloop()
