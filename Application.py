import tkinter
from CustomMenu import *
from SearchField import *
from tkinter import *
from ToolTip import *
from ProcessField import *
from DownloadDetail import *

class Application(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.root = parent
        self.init_gui()

    def on_quit(self):
        # do anything needed 
        quit()

    def init_gui(self):
        self.root.title('下载君')
        self.root.minsize(800,600)
        
        # adjust self properities
        self.pack(expand="yes")

        # add menu
        self._memu = CustomMenu(self.root)

        # add components
        self._searchField = SearchField(self)
        self._searchField.pack()

        ttk.Separator(self, orient='horizontal').pack()

        self._processField = ProcessField(self)
        self._processField.pack()

        self._downloadDetail = DownloadDetail(self)
        self._downloadDetail.pack()


if __name__ == '__main__':
    mainFrame = tkinter.Tk()

    Application(mainFrame)
    mainFrame.mainloop()