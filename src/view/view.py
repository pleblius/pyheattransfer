import tkinter as tk
import menuframe
import menubar
import mainview
"""A module to control the display for the application.
    
Initiates the main window and draw loop, then calls all necessary
modules and functions to draw the application to the screen."""

#  Initialize application window
width, height = 800, 600
display_window = tk.Tk()
display_window.geometry(f"{width}x{height}")

#  Generate menubar at the top of the window
menu_bar = menubar.generate_menu_bar(display_window)

#  Generate grid to hold application window and application menu frames


display_window.mainloop()
