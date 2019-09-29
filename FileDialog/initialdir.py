from tkinter import *
import tkinter.ttk as ttk
import tkinter.filedialog as filedialog
import os


class FiledialogInitialDirSampleApp(ttk.Frame):

    def __init__(self, app):
        super().__init__(app)
        self.pack()

        # Widget用変数を定義
        self.filename = StringVar()

        label = ttk.Label(self,text="File名")
        label.pack(side="left")
        # textvariableにWidget用の変数を定義することで変数の値が変わるとテキストも動的に変わる
        filenameEntry = ttk.Entry(self,text="",textvariable= self.filename)
        filenameEntry.pack(side="left")

        button = ttk.Button(self,text="open",command = self.openFileDialog )
        button.pack(side="left")

    #ファイルダイアログを開いてfilenameEntryに反映させる
    def openFileDialog(self):
        #スクリプト自身のファイルパスのディレクトリの取得
        initdir = os.path.dirname(__file__)
        #初期ディレクトリとして自身の親ディレクトリを指定する
        file  = filedialog.askopenfilename(initialdir=initdir)
        self.filename.set(file)


if __name__ == '__main__':
    #Tkインスタンスを作成し、app変数に格納する
    app  = Tk()
    #縦幅400横幅300に画面サイズを変更します。
    app.geometry("400x300")
    #タイトルを指定
    app.title("File Dialog Sample Program [initialdir]")
    # #フレームを作成する
    frame = FiledialogInitialDirSampleApp(app)
    # 格納したTkインスタンスのmainloopで画面を起こす
    app.mainloop()
