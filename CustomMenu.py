import tkinter
from tkinter import ttk

class CustomMenu(object):
    def __init__(self, parent):
        self.menubar = tkinter.Menu(parent)

        self.config_menu = tkinter.Menu(self.menubar)
        self.config_menu.add_command(label="下载设置", command=self.hello) 
        self.config_menu.add_command(label="一键下载", command=self.hello) 

        self.des_menu = tkinter.Menu(self.menubar)
        self.des_menu.add_command(label="如何使用", command=self.hello) 
        self.des_menu.add_command(label="获取更新", command=self.hello)
        self.des_menu.add_separator()
        self.des_menu.add_command(label="留言", command=self.hello)
        
        self.donation_menu = tkinter.Menu(self.menubar)
        self.donation_menu.add_command(label="pay1", command=self.hello)
        self.donation_menu.add_command(label="pay2", command=self.hello)

        # show menue
        self.menubar.add_cascade(label="设置", menu=self.config_menu)
        self.menubar.add_cascade(label="关于", menu=self.des_menu)
        self.menubar.add_cascade(label="捐赠", menu=self.donation_menu)
        parent.config(menu=self.menubar)

    def hello():
        print("hello world")
