import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu


class CustomerMenu():

    def __init__(self, widget):
        menubar = tkinter.Menu(self.root)

        menu_file = tkinter.Menu(self.menubar)
        menu_file.add_command(label='退出', command=self.on_quit)

        menu_edit = tkinter.Menu(self.menubar)

        menubar.add_cascade(menu=self.menu_file, label='文件')
        menubar.add_cascade(menu=self.menu_edit, label='退出')
