from tkinter import *
import tkinter.ttk as ttk


class ToolTip:
    def __init__(self, widget,messeage):
        self.widget = widget
        self.tipdialog  = None
        self.id =None
        self.messeage=messeage
        self.addEvent()

    def addEvent(self):
        self.widget.bind("<Enter>", self.focusAction)
        self.widget.bind("<Leave>", self.leaveAction)

    def leaveAction(self, event=None):
        self.cancel()
        self.hidetip()

    def focusAction(self,event):
        # 今までのをクリアして表示する
        self.cancel()
        self.id = self.widget.after(500, self.showTip)

    def cancel(self):
        id = self.id
        self.id = None
        # 予約されたアクションを取り消す
        if id:
            self.widget.after_cancel(id)

    #説明テキストの表示
    def showTip(self):
        # 既に表示されてる場合は処理の必要なし
        if self.tipdialog:
            return
        # Widget幅の1/3程度右方向に離す
        x = self.widget.winfo_rootx() + self.widget.winfo_width()/3
        # ＋3与えることでWidgetと少し離す
        y = self.widget.winfo_rooty() + self.widget.winfo_height()+3
        self.tipdialog = Toplevel(self.widget)
        # □ｘボタンのバーは必要ない
        self.tipdialog.wm_overrideredirect(True)
        # ダイアログの位置を指定
        self.tipdialog.wm_geometry("+%d+%d" % (x, y))
        # 背景白で左寄せ
        label = Label(self.tipdialog, text=self.messeage, justify=LEFT,
                      background="#ffffff")
        label.pack()

    def hidetip(self):
        tw = self.tipdialog
        self.tipdialog = None
        if tw:
            tw.destroy()
class ToolTipSample(ttk.Frame):
    def __init__(self ,master):
        super().__init__(master)
        label = Label(self, text="ボタンにマウスをかざしてください")

        label.pack()
        button = ttk.Button(self,text="toolTip")
        button.pack()
        ToolTip(button,"このチップはボタンテスト")
        ToolTip(label,"このチップはラベルテスト")
        self.pack()


if __name__ == '__main__':
    master = Tk()
    master.title("ToolTipSample")
    master.geometry("300x100")
    ToolTipSample(master)
    master.mainloop()
