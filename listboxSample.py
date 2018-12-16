from tkinter import *
import tkinter.ttk as ttk

class ListboxSampleApp(ttk.Frame):


    def __init__(self, app):
        super().__init__(app)
        self.pack()
        self.countrynames = ('Argentina', 'Australia', 'Belgium', 'Brazil', 'Canada', 'China', 'Denmark', \
                                'Finland', 'France', 'Greece', 'India', 'Italy', 'Japan', 'Mexico', 'Netherlands', 'Norway', 'Spain', \
                                'Sweden', 'Switzerland')
        cnames = StringVar(value=self.countrynames)
        snames = StringVar()

        self.listbox  =  Listbox(app, listvariable=cnames, height=5)
        self.listbox.pack()

        button = ttk.Button(app,text = "選択↓" ,command=self.selectItem)
        button.pack()

        self.selectbox = Listbox(app, listvariable=snames, height=5)
        self.selectbox.pack()
    def selectItem(self):
        # 選択されている数値インデックスを含むリストを取得
        itemIdxList =  self.listbox.curselection()
        if len(itemIdxList) == 1:
            country = self.countrynames[itemIdxList[0]]
            # 末尾に選択された要素を追加する
            self.selectbox.insert("end",country)





if __name__ == '__main__':
    #Tkインスタンスを作成し、app変数に格納する
    app  = Tk()
    #縦幅600横幅300に画面サイズを変更します。
    app.geometry("600x300")
    #タイトルを指定
    app.title("Listbox Sample Program")
    # #フレームを作成する
    frame = ListboxSampleApp(app)
    # 格納したTkインスタンスのmainloopで画面を起こす
    app.mainloop()
