import tkinter.messagebox as messagebox
from tkinter import *
import tkinter.ttk as ttk
from dbview import DBView
import sqlite3
import os

class DBLogic:
    """
    DBViewer読み込み、書き込みロジック
    """

    def __init__(self):
        """
        列とレコード用の配列を初期化
        """
        self.header =[]
        self.data =[]
        self.db_path=""
        self.table=""

    def readDB(self,db_path):
        """
        csvを読み込んで内部にデータを反映する
        1行目を列名、他の行をデータとして取得する
        """
        table_list = []
        self.db_path = db_path
        try :
            connection = sqlite3.connect(db_path)
            cursor = connection.cursor()
            cursor.execute("select name from sqlite_master where type='table'")
            table_list=[data for data in cursor.fetchall()]
            connection.close()
        except sqlite3.Error as e:
            print('sqlite3 Error:', e)

        return table_list
    def readColumn(self,table_name):
        self.table_name = table_name
        column=[]
        try :
            connection = sqlite3.connect(self.db_path)
            cursor = connection.cursor()
            cursor.execute("select * from " + table_name)
            column=[data[0] for data in cursor.description]
            connection.close()
        except sqlite3.Error as e:
            print('sqlite3 Error:', e)
        return column
    def readData(self,table_name):
        raws=[]
        try :
            connection = sqlite3.connect(self.db_path)
            cursor = connection.cursor()
            cursor.execute("select * from " + table_name)
            raws=[data for data in cursor.fetchall()]
            connection.close()
        except sqlite3.Error as e:
            print('sqlite3 Error:', e)
        print(raws)
        return raws
    def updateRowData(self,coloumns,rows):
        ret = True
        column_size = len(coloumns)
        p =""
        pre = [column+"=?"for column in coloumns]
        r_pre = [column for column in coloumns]
        q_pre = ["?" for column in coloumns]

        p = ",".join(pre)
        r = ",".join(r_pre)
        q = ",".join(q_pre)

        update = "update "+self.table_name + " set "+p+" where id = ?"
        replace = "replace into "+self.table_name+"("+r+")" + "values("+q+")"
        print(update)
        print(replace)
        try :
            connection = sqlite3.connect(self.db_path)
            cursor = connection.cursor()
            for row in rows:
                # arg =list(row)
                # arg.append(row[0])
                # print(arg)
                # cursor.execute(update,arg)
                cursor.execute(replace,row)
            connection.commit()
            connection.close()
        except sqlite3.Error as e:
            print('sqlite3 Error:', e)
            ret = False
        return ret

class CSVControl:
    """
    csvViewerのコントローラー
    """

    def __init__(self):
        """
        アプリの立ち上げとイベント登録
        """
        master = Tk()
        master.title("SQLiteViewer")
        master.geometry("1000x400")
        self.view = DBView(master)
        self.logic = DBLogic()
        self.view.setReadButtonCommand(self.readButtonCommand)
        self.view.setTableCommand(self.readTableCommand)
        self.view.setSaveButtonCommand(self.saveButtonCommand)
        master.mainloop()

    def readButtonCommand(self):
        """
        csv読み込みボタン用コマンド
        csvから取得した列名、データをViewに反映する。
        csvが変更されるごとにRowDataフレームがリロードされるので、
        保存ボタンコマンドも再設定
        """
        file_path = self.view.getFilePath()
        table_list = self.logic.readDB(file_path)
        self.view.setTableInfo(table_list)
        # columns,datas = self.readCsv()
        # self.view.setNewColumnAndData(columns,datas)
        # self.view.setSaveButtonCommand(self.saveButtonCommand)

    def saveButtonCommand(self):
        """
        保存ボタン用コマンド
        指定されたパスにviewで指定された情報をcsv形式で書きだす
        """
        # file_path = self.view.getFilePath()
        columns = self.view.getColumns()
        rows =self.view.getRows()
        ret = self.logic.updateRowData(columns,rows)
        # ret = self.logic.writeCsv(file_path,columns,rows)
        if ret:
            messagebox.showinfo("writecsv","succeed")
        else:
            messagebox.showerror("writecsv","failed")
    def readTableCommand(self):
        table_name = self.view.getSelectTable()
        print("table_name",table_name)
        columns = self.logic.readColumn(table_name)
        datas = self.logic.readData(table_name)
        self.view.setNewColumnAndData(columns,datas)

    def readTable(self):
        """
        csv読み込んで列名とデータを返却
        """
        ret = False;
        file_path = self.view.getFilePath()
        if os.path.exists(file_path) :
            ret = self.logic.readCsv(file_path)
        if ret:
            messagebox.showinfo("readcsv","succeed")
        else:
            messagebox.showerror("readcsv","failed")
        return self.logic.getHeader(),self.logic.getData()

if __name__ == '__main__':
    control =  CSVControl()
    # control.readCsv()
