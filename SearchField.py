import tkinter
from tkinter import *
from ToolTip import *

class SearchField(ttk.Frame):
    def __init__(self, parent):   
        ttk.Frame.__init__(self, parent)   

        self._searchTxt = ttk.Entry(self);
        self._searchTxt.grid(column=0, row=0, columnspan=18)
        createToolTip(self._searchTxt, "在此输入需要解析的URL")

        self._searchButton = ttk.Button(self, text='解析',command=self.doSearch)
        self._searchButton.grid(column=18, row=0, columnspan=2)

    
    def doSearch(self):
        print("do search")



