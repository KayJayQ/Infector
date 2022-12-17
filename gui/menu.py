import tkinter as tk
from tkinter import messagebox

def show_about():
    messagebox.showinfo("信息", "版本 1.0")

def new_cmd(*args):
    pass

def open_cmd(*args):
    pass

def save_cmd(*args):
    pass

def saveas_cmd(*args):
    pass

def add_menu(root:tk.Tk):
    bar = tk.Menu(root)
    fileMenu = tk.Menu(root)
    fileMenu.add_command(label = "新建配置", accelerator="Ctrl+N", command=new_cmd)
    fileMenu.add_command(label = "打开配置", accelerator="Ctrl+O", command=open_cmd)
    fileMenu.add_command(label = "保存配置", accelerator="Ctrl+S", command=save_cmd)
    fileMenu.add_command(label = "另存为配置", accelerator="Ctrl+A", command=saveas_cmd)
    fileMenu.add_separator()
    fileMenu.add_command(label = "关闭程序", command = quit)
    bar.add_cascade(label = "文件", menu = fileMenu)
    bar.add_command(label = "关于", command=show_about)
    root.config(menu=bar)
    root.bind("<Control-n>", new_cmd)
    root.bind("<Control-o>", open_cmd)
    root.bind("<Control-s>", save_cmd)
    root.bind("<Control-a>", saveas_cmd)