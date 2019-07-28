from tkinter import *
import tkinter.ttk as ttk
from jobmanagerlogic import *

class JobManagerView(ttk.Frame):
    def __init__(self,master):
        super().__init__(master,borderwidth="20px")
        self._jobparam_list=[]
        self.createWidgets()
    def createWidgets(self):
        self._execwidget = JobExecWidget(self)
        self._execwidget.pack()
        for i in range(5):
            jobwidget = JobWidget(self,"Job {0}".format(i))
            jobwidget.pack()
            self._jobparam_list.append(jobwidget.getJobParam())

        self.pack()
    def setExecCommand(self,command):
        self._execwidget.setExecCommand(command)

    def getParallelNum(self):
        return self._execwidget.getParallelNum()

    def getJobParams(self):
        return self._jobparam_list

class JobExecWidget(ttk.Frame):
    """
    並列実行ジョブ数と、実行ボタンの提供
    """

    def __init__(self,master):
        super().__init__(master)
        self.createWidgets()

    def createWidgets(self):
        ttk.Label(self,text="Parallel Job").pack(side="left")
        self._parallel_number =IntVar(value=1)
        ttk.Spinbox(self,from_=1,to=4,textvariable=self._parallel_number,increment=1).pack(side="left")
        self.exec_button = ttk.Button(self,text="Exec")
        self.exec_button.pack(side="left")
    def setExecCommand(self,command):
        self.exec_button["command"] = command
    def getParallelNum(self):
        return self._parallel_number.get()



class JobWidget(ttk.Frame):
    """
    ジョブ単位毎のWidget
    ジョブコマンドと、進捗状況バーの提供
    """
    def __init__(self,master,text="job"):
        super().__init__(master)
        self._jobparam=None
        self.createWidgets(text)
    def createWidgets(self,text):
        label = ttk.Label(self,text=text)
        label.grid(column=0,row=0)
        button = ttk.Button(self,text="command",command=self._openCommandDialog)
        button.grid(column=1,row=0)
        variable = IntVar(value = 10)
        progressbar = ttk.Progressbar(self,length = 400,orient="horizontal",variable = variable)
        progressbar.grid(column=2,row=0)
        self._jobparam = JobParam(progressbar,"")
    def _openCommandDialog(self):
        widget = CommandWidget(self)
        widget.setCloseCommand(lambda:self._dialogClose(widget))
    def _dialogClose(self,dialog):
        self._jobparam.setCommand(dialog.getCommand())
        dialog.destroy()
    def getJobParam(self):

        return self._jobparam


class CommandWidget(Toplevel):
    """
    ジョブコマンドを入力するダイアログ
    """
    def __init__(self,master):
        super().__init__(master)
        self.title("InputCommand")
        self.geometry("300x200")
        self.grab_set()
        self.createWidgets()
    def createWidgets(self):
        frame = ttk.Frame(self,borderwidth="10px")
        frame.pack()
        ttk.Label(frame,text="command").pack(side="left")
        self._command = StringVar()
        ttk.Entry(frame,textvariable = self._command).pack(side="left")
        self._close_button = ttk.Button(frame,text="close")
        self._close_button.pack(side="left")
    def getCommand(self):
        return self._command.get()
    def setCloseCommand(self,command):
        self._close_button["command"] = command

if __name__ == '__main__':
    master = Tk()
    master.geometry("800x300")
    master.title("JobManagerSample")
    JobManagerView(master)
    master.mainloop()
