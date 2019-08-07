from tkinter import *


class ResizeDialog(object):

    def __init__(self, values):

        self.values = values

        self.dlg = Toplevel()

        self.dlg.title("Resize")

        self.dlg.grab_set()

        self.width_label = Label(self.dlg, text="Width")
        self.width_label.grid(row=0, column=0, padx=4, pady=4, sticky=W)

        self.width_box = Entry(self.dlg)
        self.width_box.grid(row=0, column=1, padx=4, pady=4, sticky=W)

        self.height_label = Label(self.dlg, text="Height")
        self.height_label.grid(row=1, column=0, padx=4, pady=4, sticky=W)

        self.height_box = Entry(self.dlg)
        self.height_box.grid(row=1, column=1, padx=4, pady=4, sticky=W)

        self.ok_button = Button(self.dlg, text='OK', command=self.ok)
        self.ok_button.grid(row=2, column=0, columnspan=2, padx=4, pady=4, sticky=W+E)

        self.cancel_button = Button(self.dlg, text='Cancel', command=self.cancel)
        self.cancel_button.grid(row=3, column=0, columnspan=2, padx=4, pady=4, sticky=W+E)


    def ok(self):

        self.values["width"] = int(self.width_box.get())
        self.values["height"] = int(self.height_box.get())

        self.dlg.destroy()


    def cancel(self):

        self.values["width"] = 0
        self.values["height"] = 0

        self.dlg.destroy()
