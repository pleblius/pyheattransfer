import tkinter as tk

class MenuFrame(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master=master)
        self.controller = controller

        title = tk.Label(text='Menu', master=self)
        title.pack()

        self.add_button("Create Wall", func=self.create_wall())

    def add_button(self, label, func):
        button = tk.Button(
            master=self,
            text=label,
            width=30,
            height=10,
            bg="gray",
            fg="black"
        )

        button.bind("<Button-1>", func)
        button.pack()

    def create_wall(self):
        self.controller.create_wall()
