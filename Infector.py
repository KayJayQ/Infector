import tkinter as tk
from gui import menu
from gui import option

root = tk.Tk()
root.geometry("1280x1050+200+200")
root.title("Infector")

menu.add_menu(root)

option_pane = tk.PanedWindow(showhandle=True, sashrelief="sunken")
option_pane.pack(fill = "both", expand = 1)

option_frame = tk.Frame(option_pane)
option.config_option(option_frame)
option_pane.add(option_frame)

right_pane = tk.PanedWindow(orient="vertical", showhandle=True, sashrelief="sunken")
option_pane.add(right_pane)
canvas_frame = tk.Frame(right_pane)
plot_frame = tk.Frame(right_pane)
right_pane.add(canvas_frame)
right_pane.add(plot_frame)

root.mainloop()