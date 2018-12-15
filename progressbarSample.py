from tkinter import *
import tkinter.ttk as ttk

class ProgressBarSampleApp(ttk.Frame):

    def __init__(self, app):
        super().__init__(app)
        self.pack()

        # Widget用変数を定義
        # label = ttk.Label(self,text="Progressbar")
        # label.pack(side="left")
        #
        #
        # self.pbDeterminateVer = ttk.Progressbar(self, orient=HORIZONTAL, length=200, mode='determinate')
        # self.pbDeterminateVer.pack(side="left")
        # startbutton = ttk.Button(self,text="start",command = self.startDeterminateVer)
        # startbutton.pack(side="left")
        # stopbutton = ttk.Button(self,text="stop",command = self.stopDeterminateVer)
        # stopbutton.pack(side="left")

        label = ttk.Label(self,text="Progressbar不確定モード")
        label.pack(side="left")
        self.pbIndeterminateVer = ttk.Progressbar(self, orient=HORIZONTAL, length=200, mode='indeterminate')
        self.pbIndeterminateVer.pack(side="left")
        startbutton = ttk.Button(self,text="start",command = self.startIndeterminateVer)
        startbutton.pack(side="left")
        stopbutton = ttk.Button(self,text="stop",command = self.stopIndeterminateVer)
        stopbutton.pack(side="left")


    #ファイルダイアログを開いてfilenameEntryに反映させる
    def startIndeterminateVer(self):
        self.pbIndeterminateVer.start(10)

    def stopIndeterminateVer(self):
        self.pbIndeterminateVer.stop()

    def startDeterminateVer(self):
        self.step()
        value = self.pbDeterminateVer["value"]
        maximum = self.pbDeterminateVer["maximum"]
        print(value,maximum)


    def stopDeterminateVer(self):
        self.pbDeterminateVer.stop()
    def step(self):
        self.pbDeterminateVer.step(10)


if __name__ == '__main__':
    #Tkインスタンスを作成し、app変数に格納する
    app  = Tk()
    #縦幅400横幅300に画面サイズを変更します。
    app.geometry("600x300")
    #タイトルを指定
    app.title("ProgressBar Sample Program")
    # #フレームを作成する
    frame = ProgressBarSampleApp(app)
    # 格納したTkインスタンスのmainloopで画面を起こす
    app.mainloop()
