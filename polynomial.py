from math import sqrt
def polynome():
    try:
        a = int(entry1.get())
        b = int(entry2.get())
        c = int(entry3.get())
        delta = b**2-4*a*c
        if delta < 0:
            returnedResult.set("L'équation n'admet pas de solution")
        elif delta == 0:
            x0 = -b/(2*a)
            returnedResult.set(f"x = {x0}")
        elif delta > 0:
            x1 = (-b-sqrt(delta))/(2*a)
            x2 = (-b+sqrt(delta))/(2*a)
            returnedResult.set(f"x1 = {x1}     x2 = {x2}")
    except:
        returnedResult.set("Veuillez entrer des valeurs pour a, b et c")

from tkinter import *
from keyboard import *

def kInput():
    if is_pressed('enter'):
        polynome()

main = Tk()
main.title("Polynomial")
main.resizable(False, False)

entry1 = Entry(main, width=10, justify=CENTER)
entry1.grid(row=0, column=0, padx=5)
txt1 = Label(main, width=10, text="x² +", justify=CENTER)
txt1.grid(row=0, column=1)
entry2 = Entry(main, width=10, justify=CENTER)
entry2.grid(row=0, column=2)
txt2 = Label(main, width=10, justify=CENTER, text="x +")
txt2.grid(row=0, column=3)
entry3 = Entry(main, width=10, justify=CENTER)
entry3.grid(row=0, column=4)
txt3 = Label(main, width=10, justify=CENTER, text="=")
txt3.grid(row=0, column=5)

returnedResult = StringVar()
txtFinal = Label(main, width=50, justify=CENTER, textvariable=returnedResult)
txtFinal.config(relief='groove')
txtFinal.grid(row=1, column=0, columnspan=5, padx=5)

resolve = Button(main, text="Resolve", command=polynome)
resolve.grid(row=1, column=5)


def shutdown():
    global run
    run = False
    main.quit()
main.protocol("WM_DELETE_WINDOW", shutdown)

run = True

while run:
    main.update()
    kInput()