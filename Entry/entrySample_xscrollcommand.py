from tkinter import *
import tkinter.ttk as ttk

class EntrySampleXScrollCommand(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()
        self.pack()

    def create_widgets(self):
        scroll = ttk.Scrollbar(self,orient='horizontal',takefocus=False)
        entry = ttk.Entry(self,xscrollcommand=scroll.set)
        # packの順番でスクロールバーの位置が変わる
        entry.pack()
        scroll.pack(fill='x')
        scroll['command'] = entry.xview


if __name__ == '__main__':
    master = Tk()
    master.title("EntrySample-xscrollcommand")
    master.geometry("400x50")
    EntrySampleXScrollCommand(master)
    master.mainloop()
