from tkinter import *
import tkinter.ttk as ttk

class NotebookSample(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()
        self.pack()

    def create_widgets(self):
        note = ttk.Notebook(self)
        note.pack()
        note0 = ttk.Frame(note,width=300,height=300)
        note1 = ttk.Frame(note,width=300,height=300)
        note.add(note0,text="note0")
        note.add(note1,text="note1")

if __name__ == '__main__':
    master = Tk()
    master.title("NotebookSample")
    master.geometry("400x400")
    NotebookSample(master)
    master.mainloop()
