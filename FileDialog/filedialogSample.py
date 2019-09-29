from tkinter import *
import tkinter.ttk as ttk
import tkinter.filedialog as filedialog

class FiledialogSampleApp(ttk.Frame):

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
        file  = filedialog.askopenfilename(filetypes=[("all files", "*"),("png","*.png"),("gif","*.gif"),("python","*.py")]);
        self.filename.set(file)


if __name__ == '__main__':
    #Tkインスタンスを作成し、app変数に格納する
    app  = Tk()
    #縦幅400横幅300に画面サイズを変更します。
    app.geometry("400x300")
    #タイトルを指定
    app.title("File Dialog Sample Program")
    # #フレームを作成する
    frame = FiledialogSampleApp(app)
    # 格納したTkインスタンスのmainloopで画面を起こす
    app.mainloop()
