import tkinter as tk
from tkinter import ttk
from databus import Databus
from modules.person import Person

class ModuleOption:

    def __init__(self, name, params):
        self.name = name
        self.params = params

        self.binaries = []

    def add_binary(self, op1:str, op2:str, varname:str, default = 1, des = ""):
        self.binaries.append((op1, op2, varname, default, des))

def set_binary(frame:tk.Frame, params:dict, op1, op2, varname, defualt, des):
    v = tk.IntVar()
    v.set(defualt)
    def set1(): params[varname] = op1
    def set2(): params[varname] = op2

    if v.get() == 1:
        set1()
    else:
        set2()

    this_frame = tk.Frame(frame)
    if len(des) > 0:
        tk.Label(this_frame, text = des).pack(side = "left")
    tk.Radiobutton(this_frame, text = op1, variable=v, value = 1, command=set1).pack(side="left")
    tk.Radiobutton(this_frame, text = op2, variable=v, value = 2, command=set2).pack(side="left")
    this_frame.pack(side="top")


def config_option(frame:tk.Frame):
    title = tk.Label(frame, text = "选项")
    title.pack()
    scroll_bar = tk.Scrollbar(frame, orient="vertical")
    scroll_bar.pack(side="right", fill="y")

    for module in Databus.active_modules:
        try:
            module_option = module.config()
            startline = ttk.Separator(frame, orient = "horizontal")
            startline.pack(padx = 10, fill='x')
            title = tk.Label(frame, text = module.name).pack(side = "top")

            for op1, op2, var, defualt, des in module_option.binaries:
                set_binary(frame, module_option.params, op1, op2, var, defualt, des)

            endline = ttk.Separator(frame, orient = "horizontal")
            endline.pack(padx = 10, fill='x')

        except NotImplementedError:
            continue