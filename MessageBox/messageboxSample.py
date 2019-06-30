from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as messagebox

class MessageBoxSampleApp(ttk.Frame):

    def __init__(self, app):
        super().__init__(app)
        self.pack()

        infoButton = ttk.Button(self,text="info",command = self.infomationMessage)
        infoButton.pack()
        errorButton = ttk.Button(self,text="error",command = self.errorMessage)
        errorButton.pack()
        warningButton = ttk.Button(self,text="warnning",command = self.warningMessage)
        warningButton.pack()



    def infomationMessage(self):
        messagebox.showinfo("infomation message", "情報メッセージダイアログ")

    def errorMessage(self):
        messagebox.showerror("error message", "エラーメッセージダイアログ")

    def warningMessage(self):
        messagebox.showwarning("warning message", "エラーメッセージダイアログ")



if __name__ == '__main__':
    #Tkインスタンスを作成し、app変数に格納する
    app  = Tk()
    #縦幅400横幅300に画面サイズを変更します。
    app.geometry("400x300")
    #タイトルを指定
    app.title("MessageBox Sample Program")
    # #フレームを作成する
    frame = MessageBoxSampleApp(app)
    # 格納したTkインスタンスのmainloopで画面を起こす
    app.mainloop()
