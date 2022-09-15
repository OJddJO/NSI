def c2f():
    celsius = float(degree1.get())
    fahrenheit = (celsius*9/5)+32
    txt.set(str(fahrenheit)+'°F')

def f2c():
    fahrenheit = float(degree1.get())
    celsius = (fahrenheit-32)/9*5
    txt.set(str(celsius)+'°C')

def c2k():
    celsius = float(degree1.get())
    kelvin = celsius+273
    txt.set(str(kelvin)+'K')

def k2c():
    kelvin = float(degree1.get())
    celsius = kelvin-273
    txt.set(str(celsius)+'°C')

def k2f():
    kelvin = float(degree1.get())
    fahrenheit = ((kelvin-273)*9/5)+32
    txt.set(str(fahrenheit)+'°F')

def f2k():
    fahrenheit = float(degree1.get())
    kelvin = (fahrenheit-32)/9*5+273
    txt.set(str(kelvin)+'K')

from tkinter import *

#création de la fenetre tkinter
root = Tk()
root.title("Temperature Converter")
root.resizable(False, False)

#création d'une entry box
degree1 = Entry(root, width=50, justify=CENTER)
degree1.grid(row=1, column=0)

#variable tkinter pour sortie
txt = StringVar()
txt.set('')
#affiche la variable txt
degree2 = Label(root, width=50, textvariable=txt)
degree2.grid(row=4, column=0)

#création des boutons de convertions
FtoC = Button(root, text='°F2°C', command=f2c)
FtoC.grid(row=1, column=1)
CtoF = Button(root, text='°C2°F', command=c2f)
CtoF.grid(row=0, column=1)
KtoF = Button(root, text='K2°F', command=k2f)
KtoF.grid(row=2, column=1)
FtoK = Button(root, text='°F2K', command=f2k)
FtoK.grid(row=3, column=1)
CtoK = Button(root, text='°C2K', command=c2k)
CtoK.grid(row=4, column=1)
KtoC = Button(root, text='K2°C', command=k2c)
KtoC.grid(row=5, column=1)

#remplace la fx du bouton fermer
def shutdown():
    global run
    run = False
    root.quit()
root.protocol("WM_DELETE_WINDOW", shutdown)

#run
run = True

while run:
    root.update()