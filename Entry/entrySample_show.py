from tkinter import *
import tkinter.ttk as ttk

class EntrySampleShow(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.password = StringVar()
        self.value = StringVar()
        self.create_widgets()
        self.pack()

    def create_widgets(self):
        inputFrame = ttk.Frame(self)
        inputFrame.pack()

        entry = ttk.Entry(inputFrame,show='*',textvariable=self.password)
        entry.pack(side="left")

        button = ttk.Button(inputFrame,text="submit",command = self.submitCommand)
        button.pack(side="left")

        passwordValueLabel = ttk.Label(self,textvariable=self.value)
        passwordValueLabel.pack()

    def submitCommand(self):
        password = self.password.get()
        self.value.set(password)


if __name__ == '__main__':
    master = Tk()
    master.title("EntrySample-show")
    master.geometry("300x50")
    EntrySampleShow(master)
    master.mainloop()
