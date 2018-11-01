import tkinter
from tkinter import *
from ToolTip import *

class ProcessField(ttk.Frame):
    def __init__(self, parent):   
        ttk.Frame.__init__(self, parent)   

        self._title = ttk.Label(self, text='xxxx title yyy zzz')
        self._title.grid(column=0, row=0, rowspan=2, columnspan=10, sticky='nsew')

        self._processBar = ttk.Label(self, text='this a bar')
        self._processBar.grid(column=0, row=2, rowspan=3, columnspan=10, sticky='nsew')

        self._actionButtonFrame = ttk.LabelFrame(self, text='')
        self._actionButtonFrame.grid(column=10, row=0, rowspan=4, sticky='nsew')

        # add sub buttons
        self._actionButtonFrame._openBtn = ttk.Button(self._actionButtonFrame, text='打开', command=self.doSearch)
        self._actionButtonFrame._openBtn.grid(column=0, row=0)

        self._actionButtonFrame._cancelBtn = ttk.Button(self._actionButtonFrame, text='取消', command=self.doSearch)
        self._actionButtonFrame._cancelBtn.grid(column=0, row=1)

        self._actionButtonFrame._viewBtn = ttk.Button(self._actionButtonFrame, text='预览', command=self.doSearch)
        self._actionButtonFrame._viewBtn.grid(column=0, row=2)

    
    def doSearch(self):
        print("do search")



