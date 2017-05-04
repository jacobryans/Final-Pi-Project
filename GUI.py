# GUI file that handles the status on the GUI
# Will handle the sounds and art (background changing etc.) aswell, to be incorporated
from Tkinter import *
from Defs import *
class GUI(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

    def createGui(self):
        img = PhotoImage(file="blank.gif")
        image = Label(image=img)
        image.pack(side=LEFT)

        listbox = Listbox(window)
        listbox.grid(sticky=W)
        listbox.pack()

        listbox.insert(END, "Inventory")

        g = 1
        for i in range(0, 16):
            listbox.insert(END, g)
            g = g + 1

    def start(self):
        self.createGui()
    

window = Tk()
window.geometry('700x500')

gui = GUI(window)
gui.start()

window.mainloop()


        
