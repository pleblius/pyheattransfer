import tkinter as tk
import src.controller as controller

def generate_menu_bar(window: tk.Tk):
    """Generates a new menu bar at the top of the application window.

    The menu bar generated will contain multiple cascading menus, similar to standard Windows applications.
    TODO: IMPLEMENT ALL MENU OPTIONS AND COMMANDS
    TODO: ADD LIST OF MENU OPTIONS"""

    #  Link menubar to main window
    menubar = tk.Menu(window)
    window.config(menu=menubar)

    menubar.add_cascade(label='File', menu=generate_file_menu(menubar))
    menubar.add_cascade(label='Edit', menu=generate_edit_menu(menubar))
    menubar.add_cascade(label='View', menu=generate_view_menu(menubar))
    menubar.add_cascade(label='Options', menu=generate_options_menu(menubar))
    menubar.add_cascade(label='Tools', menu=generate_tools_menu(menubar))
    menubar.add_cascade(label='Help', menu=generate_help_menu(menubar))

    return menubar

def generate_file_menu(menubar):
    """Generates the File cascading menu option for the menu bar.

    Contains commands to generate a new application, save the current application, open a previously saved application,
    and to exit the program.
    TODO: IMPLEMENT NECESSARY COMMANDS"""

    filemenu = tk.Menu(menubar, tearoff=False)

    filemenu.add_command(label='New')
    filemenu.add_command(label='Save')
    filemenu.add_command(label='Load')
    filemenu.add_separator()
    filemenu.add_command(label='Exit', command=menubar.master.destroy)

    return filemenu

def generate_edit_menu(menubar):
    pass

def generate_view_menu(menubar):
    pass

def generate_tools_menu(menubar):
    pass

def generate_help_menu(menubar):
    pass

def generate_options_menu(menubar):
    pass