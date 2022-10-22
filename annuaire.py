import os
from tkinter import *
from tkinter.ttk import *

class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        if not os.path.isfile('annuaire.txt'):
            open("annuaire.txt", 'w').write(r"{}")
        self.menu()
        self.addContactToTreeview()


    def menu(self):
        self.title("Contact")
        self.resizable(False, False)
        
        self.column = ("name", "number")
        self.annuaire = Treeview(self, column=self.column, show='headings', selectmode='browse')
        self.annuaire.heading("name", text="Contact Name")
        self.annuaire.heading("number", text="Phone Number")
        self.annuaire.pack()
        
        self.mainMenu = Menu(self)
        self.config(menu=self.mainMenu)
        self.mainMenu.add_command(label="Add Contact", command=self.addContact)
        self.mainMenu.add_command(label="Reload Contact", command=self.addContactToTreeview)


    def addContactToTreeview(self):
        path = "annuaire.txt"

        def readData():
            data = open(path, 'r').read()
            data = eval(data)
            return data
        dictionnary = readData()
        
        for item in self.annuaire.get_children():
            self.annuaire.delete(item)

        for element in dictionnary:
            tmp = (element, dictionnary[element])
            self.annuaire.insert('', END, values=tmp)


    def addContact(self):
        path = "annuaire.txt"

        self.addContactWin = Toplevel(self)
        self.addContactWin.title("Add Contact")
        self.resizable(False, False)

        self.nameFrame = LabelFrame(self.addContactWin, text="Name")
        self.nameFrame.grid(row=0)
        self.nameVariable = StringVar()
        self.nameEntry = Entry(self.nameFrame, textvariable=self.nameVariable, width=40)
        self.nameEntry.pack()

        self.numberFrame = LabelFrame(self.addContactWin, text="Phone Number")
        self.numberFrame.grid(row=1)
        self.phoneNumber = StringVar()
        self.numberEntry = Entry(self.numberFrame, textvariable=self.phoneNumber, width=40)
        self.numberEntry.pack()

        def readData():
            data = open(path, 'r').read()
            data = eval(data)
            return data

        def writeData():
            data = (self.nameVariable.get(), self.phoneNumber.get())
            dictionnary = readData()
            dictionnary[data[0]] = data[1]
            open(path, 'w').write(str(dictionnary))
            print("Contact Added")

        self.validButton = Button(self.addContactWin, text="Valid", command=writeData)
        self.validButton.grid(row=2)

        def shutdown():
            self.addContactWin.destroy()
            self.addContactToTreeview()
        self.addContactWin.protocol("WM_DELETE_WINDOW", shutdown)
        self.addContactWin.mainloop()


app = App()
app.mainloop()
