import tkinter as tk
import src.state as state, src.controller as controller
from src.view import appframe as af, menuframe as mf, menubar as mb, popupwindow as pw
"""A module to control the display for the application.

Initiates the main window and draw loop, then calls all necessary
modules and functions to draw the application to the screen."""

#  Initial setup
state = state.State()
controller = controller.Controller(state)

#  Initialize application window
width, height = 800, 600
window = tk.Tk()
window.geometry(f"{width}x{height}")

#  Generate mboptions at the top of the window
menubar = mb.MenuBar(window)
window.config(menu=menubar)

#  Generate grid to hold application window and application menu frames
appframe = af.AppFrame(master=window)
appframe['borderwidth'] = 4
appframe['relief'] = 'sunken'
appframe.grid(row=0, column=0, sticky="nsw")

menuframe = mf.MenuFrame(master=window, controller=controller)
menuframe['borderwidth'] = 4
menuframe['relief'] = 'flat'
menuframe.grid(row=0, column=1, sticky="nse")

window.columnconfigure([0, 1], weight=1, minsize=250)
window.rowconfigure(0, weight=1, minsize=300)

window.mainloop()
