from modules.module import Module
from gui import option

class Person(Module):

    name = "人群"
    params = dict()

    def __init__(self):
        super()
        self.alive = True

    def config():
        ops = option.ModuleOption("人群", Person.params)
        ops.add_binary("male", "female", "Gender", 1, "指定人群性别")
        return ops
