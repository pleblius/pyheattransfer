import tkinter as tk
"""This represents a MenuBar object, an extension of the tkinter menu class. Contains all of the cascading
menu options necessary for the heat transfer application"""


class MenuBar(tk.Menu):
    def __init__(self, master):
        super().__init__(master=master)

        self.generate_file()
        self.generate_edit()
        self.generate_view()

    def generate_file(self):
        """Generates the File cascading menu, containing options for file manipulation.

        New generates a new file.
        Save saves the current file.
        Open loads a previously saved file.
        Exit terminates the application."""

        file_menu = tk.Menu(master=self, tearoff=False)

        #  TODO: Implement commands
        file_menu.add_command(label='New')
        file_menu.add_command(label='Save')
        file_menu.add_command(label='Load')
        file_menu.add_separator()
        file_menu.add_command(label='Exit', command=self.master.destroy)

        self.add_cascade(label='File', menu=file_menu)

    def generate_edit(self):
        """Generates the Edit cascading menu, containing options to edit the application and the objects
        in it.

        Materials opens a new window to edit material properties.
        Options opens a new window to edit document options"""

        edit_menu = tk.Menu(master=self, tearoff=False)

        #  TODO: Implement commands
        edit_menu.add_command(label='Materials')
        edit_menu.add_command(label='Options')

        self.add_cascade(label='Edit', menu=edit_menu)

    def generate_view(self):
        """Generates the View cascading menu, with options to edit the view properties for the application.

        Mode opens a popup to toggle the view between setup and heat-map.
        Plot generates a new tempature plot for a given object."""

        view_menu = tk.Menu(master=self, tearoff=False)

        #  TODO: Implement Commands
        view_menu.add_command(label='Mode')
        view_menu.add_command(label='Plot')

        self.add_cascade(label='View', menu=view_menu)
