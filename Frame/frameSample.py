from tkinter import *
import tkinter.ttk as ttk

class FrameSampleApp(ttk.Frame):


    def __init__(self, app):
        super().__init__(app)
        self.pack()
        firstFrame =ttk.Frame(app,width =600,height=300)
        firstFrame.pack()

        flatframe = ttk.Frame(firstFrame,width =200,height=200,padding=(5,10),borderwidth=30,relief="flat")
        flatframe.pack(side ="left")
        flatframe.propagate(False)
        flatlabel = ttk.Label(flatframe,text="relief=flat")
        flatlabel.pack()

        grooveframe = ttk.Frame(firstFrame,width =200,height=200,padding=(5,10),borderwidth=30,relief="groove")
        grooveframe.pack(side ="left")
        grooveframe.propagate(False)
        groovelabel = ttk.Label(grooveframe,text="relief=groove")
        groovelabel.pack()

        raisedframe = ttk.Frame(firstFrame,width =200,height=200,padding=(5,10),borderwidth=30,relief="raised")
        raisedframe.pack(side ="left")
        raisedframe.propagate(False)
        raisedlabel = ttk.Label(raisedframe,text="relief=raised")
        raisedlabel.pack()

        secoundFrame =ttk.Frame(app,width =600,height=300)
        secoundFrame.pack()

        ridgeframe = ttk.Frame(secoundFrame,width =200,height=200,padding=(5,10),borderwidth=30,relief="ridge")
        ridgeframe.pack(side ="left")
        ridgeframe.propagate(False)
        ridgelabel = ttk.Label(ridgeframe,text="relief=ridge")
        ridgelabel.pack()

        solidframe = ttk.Frame(secoundFrame,width =200,height=200,padding=(5,10),borderwidth=30,relief="solid")
        solidframe.pack(side ="left")
        solidframe.propagate(False)
        solidlabel = ttk.Label(solidframe,text="relief=solid")
        solidlabel.pack()

        sunkenframe = ttk.Frame(secoundFrame,width =200,height=200,padding=(5,10),borderwidth=30,relief="sunken")
        sunkenframe.pack(side ="left")
        sunkenframe.propagate(False)
        sunkenlabel = ttk.Label(sunkenframe,text="relief=sunken")
        sunkenlabel.pack()





if __name__ == '__main__':
    #Tkインスタンスを作成し、app変数に格納する
    app  = Tk()
    #縦幅600横幅300に画面サイズを変更します。
    app.geometry("600x400")
    #タイトルを指定
    app.title("Frame Sample Program")
    # #フレームを作成する
    frame = FrameSampleApp(app)
    # 格納したTkインスタンスのmainloopで画面を起こす
    app.mainloop()
