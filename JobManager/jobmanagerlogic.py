from multiprocessing import Pool
import subprocess
from tkinter import *
import tkinter.ttk as ttk
class JobParam:
    def __init__(self,progressbar,command):
        self.progressbar = progressbar
        self.command = command

class JobManagerControl:
    def __init__(self):
        master = Tk()
        master.geometry("800x600")
        master.title("JobManager")
        self.logic = JobManagerLogic()
        self.view = JobManagerView(master)

        master.mainloop()

    def execCommand(self):
        self.jobParams = self.view.getJobParams()
        self.parallel = self.view.getParallelNum()
        thread = Pool(self.parallel)
        thread.map(self.exec,self.jobParams)

    def exec(self,jobparam):
        progressbar = jobparam.progressbar
        command = jobparam.command
        progressbar["mode"] ='indeterminate'
        progressbar.start(10)
        ret = self.logic(command)
        progressbar["mode"] ='determinate'
        if ret:
            progressbar.set(99);

class JobManagerLogic:

    def __init__(self):
        pass
        """
        外部プロセスの起動
        """
    def exec(self,command):
        print("testcommand",command)
        return subprocess.call(command)
