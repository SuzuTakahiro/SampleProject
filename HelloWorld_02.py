from tkinter import *
import tkinter.ttk as ttk

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
    #格納したTkインスタンスのmainloopで画面を起こす
    app.mainloop()
