from tkinter import *
import tkinter.ttk as ttk

class NotebookStateSample(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()
        self.pack()

    def create_widgets(self):
        note = ttk.Notebook(self)
        note.pack()
        self.note = note
        note0 = ttk.Frame(note,width=300,height=300)
        note1 = ttk.Frame(note,width=300,height=300)
        note2 = ttk.Frame(note,width=300,height=300)
        note.add(note0,text="note0",state="normal")
        note.add(note1,text="note1",state="disabled")
        note.add(note2,text="note2",state="hidden")
        normalButton = ttk.Button(self,text="normal",command=self.normalCommand)
        normalButton.pack()
        disabledButton = ttk.Button(self,text = "disabled",command=self.disabledCommand)
        disabledButton.pack()
        hiddenButton = ttk.Button(self,text = "hidden",command=self.hiddenCommand)
        hiddenButton.pack()
        print(note.tabs())

    def normalCommand(self):
        self.note.tab(tab_id=2,state="normal")
    def disabledCommand(self):
        self.note.tab(tab_id=2,state="disabled")
    def hiddenCommand(self):
        self.note.tab(tab_id=2,state="hidden")


if __name__ == '__main__':
    master = Tk()
    master.title("NotebookStateSample")
    master.geometry("400x400")
    NotebookStateSample(master)
    master.mainloop()
