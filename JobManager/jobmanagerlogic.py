import concurrent.futures as futures
import subprocess
from tkinter import *
import tkinter.ttk as ttk
from jobmanager import *
import time

class JobParam:
    """
    実行コマンドは都度変更があるが、
    プログレスバーは生成時に設定されるだけでいいためセッターは必要ない
    """
    def __init__(self,progressbar,command):
        self._progressbar = progressbar
        self._command = command

    def getProgressBar(self):
        return self._progressbar

    def setCommand(self,command):
        self._command = command

    def getCommand(self):
        return self._command




class JobManagerControl:
    def __init__(self):
        master = Tk()
        master.geometry("800x300")
        master.title("JobManager")
        self.logic = JobManagerLogic(self)
        self.view = JobManagerView(master)
        self.view.setExecCommand(self.execCommand)
        master.mainloop()

    def execCommand(self):
        self.jobParams = self.view.getJobParams()
        self.parallel = self.view.getParallelNum()
        # self.exec(self.jobParams[0])
        # self.jobParams[0].getProgressBar().set(40)
        executor = futures.ThreadPoolExecutor(max_workers=self.parallel)
        future_list=[]
        for job in self.jobParams:
            future_list.append(executor.submit(self.exec,job.getCommand(),job.getProgressBar()))
        # for fu in future_list:
            # print(fu.result())
        executor.shutdown(wait=False)
        # executor.submit(self.exec,self.jobParams[0].getCommand(),self.jobParams[0].getProgressBar())
        # executor.submit(self.exec,self.jobParams[1].getCommand(),self.jobParams[1].getProgressBar())
        # for job in self.jobParams:


    def exec(self,command,progressbar):
        progressbar["mode"] ='indeterminate'
        progressbar.start(10)
        ret = self.logic.exec(command)
        progressbar.stop()


class JobManagerLogic:

    def __init__(self,control):
        """
        外部プロセスの起動
        """
    def exec(self,job):
        time.sleep(3)
        if job !="":
            print(job)
            print(job.split())
            proc = subprocess.call(job,shell=True)
            print(proc)

        return True
        # print(self.control.jobParams[job])

        # return subprocess.call(command)
if __name__ == '__main__':
    JobManagerControl()
