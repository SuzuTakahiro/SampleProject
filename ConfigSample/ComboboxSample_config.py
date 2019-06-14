from tkinter import *
import tkinter.ttk as ttk
import configparser
import json
import os

class ConfigValuesSample(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.label_values="label"
        self.fruit_values=""
        self.load_config()
        self.create_widgets()
        self.pack()

    """
    config.iniから読み取った値を各Widgetのオプションに与える
    """
    def create_widgets(self):
        label = ttk.Label(text=self.label_values)
        label.pack()
        combo = ttk.Combobox(self,values=self.fruit_values)
        combo.pack()

    """
    このファイルのパスからconfig.iniファイルのパスを取得し、UTF-8で読み込む
    json.loadsを使用すること(loadではない)
    """
    def load_config(self):
        path =os.path.join(os.path.dirname(__file__),"config/config.ini")
        config = configparser.ConfigParser()
        config.read(path,"UTF-8")
        self.label_values = config["settings"]["label"]
        self.fruit_values=json.loads(config["settings"]["fruitvalues"])

if __name__ == '__main__':
    master = Tk()
    master.title("ConfigValuesSample")
    master.geometry("300x200")
    ConfigValuesSample(master)
    master.mainloop()
