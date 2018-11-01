import tkinter
from tkinter import *
from ToolTip import *

class DownloadDetail(ttk.Frame):
    def __init__(self, parent):   
        ttk.Frame.__init__(self, parent)   

        # todo: image='xxxx'
        self._image = ttk.Label(self, text="xxx image")
        self._image.grid(column=0, row=0, rowspan=10, columnspan=8, sticky='nsew')

        # add detail info
        self.initDetailsInfo()

        # choose which format of video to download
        self.initVideoConfig()

        # download button
        self._beginBtn = ttk.Button(self, text='开始下载', command=self.doSearch)
        self._beginBtn.grid(column=0, row=11, columnspan=16, sticky='nsew')
    

    def initDetailsInfo(self):
        self._detailsFrame = ttk.LabelFrame(self, text='')
        self._detailsFrame.grid(column=8, row=0, rowspan=10, columnspan=8, sticky='nsew')

        self._detailsFrame._title = ttk.Label(self._detailsFrame, text='title xxx')
        self._detailsFrame._title.grid(column=0, row=0, rowspan=2, sticky='nsew')

        self._detailsFrame._author = ttk.Label(self._detailsFrame, text='author xxx')
        self._detailsFrame._author.grid(column=0, row=2, sticky='nsew')

        self._detailsFrame._createDate = ttk.Label(self._detailsFrame, text='create Date xxx')
        self._detailsFrame._createDate.grid(column=0, row=3, sticky='nsew')

        self._detailsFrame._tags = ttk.Label(self._detailsFrame, text='xxx | yyy | zzz')
        self._detailsFrame._tags.grid(column=0, row=4, sticky='nsew')
    

    def initVideoConfig(self):
        self._videoConfigFrame = ttk.LabelFrame(self, text='')
        self._videoConfigFrame.grid(column=0, row=10, sticky='nsew')
    

    def doSearch(self):
        print("do search")



