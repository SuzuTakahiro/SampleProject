import csv
import tkinter.messagebox as messagebox
from tkinter import *
import tkinter.ttk as ttk
from csvview import CSVView

class CSVLogic:

    def __init__(self):
        self.header =[]
        self.data =[]

    def readCsv(self,data_path):
        ret = True
        header = []
        data =[]
        try :
            csv_file = open(data_path, "r",newline="")
            f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\n", quotechar='"', skipinitialspace=True)
            header = next(f)
            print(header)
            for row in f:
                data.append(row)
            csv_file.close()
        except IOError as e:
            print(e)
            ret = False
        self.header = header
        self.data = data
        return ret
    def writeCsv(self):
        pass
    def getHeader(self):
        return self.header
    def getData(self):
        return self.data


class CSVControl:

    def __init__(self):
        master = Tk()
        master.title("CsvViewer")
        master.geometry("1000x400")
        self.view = CSVView(master)
        self.logic = CSVLogic()
        self.view.setReadButtonCommand(self.readCsv)
        master.mainloop()

    def readCsv(self):
        print("aaa")
        print(self.view.getFilePath())
        ret = self.logic.readCsv(r"C:\Users\ponta\GitHub\SampleProject\CsvViewer\test.csv")
        if ret:
            messagebox.showinfo("readcsv","succeed")
        return self.logic.getHeader(),self.logic.getData()

if __name__ == '__main__':
    control =  CSVControl()
    # control.readCsv()
