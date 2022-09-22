def bissextile():
    try:
        n = int(date.get())
        if n%4==0 and (n//100)%4==0:
            tmp = "Is Bissextile"
        else:
            tmp = "Is Not Bissextile"
        txt.set(tmp)
    except:
        txt.set("The value isn't an integer")


from tkinter import *
from keyboard import *

def kInput():
    if is_pressed('enter'):
        bissextile()

main = Tk()
main.resizable(False, False)
main.title("Bissextile")

date = Entry(main, width=25, justify=CENTER)
date.grid(row = 1, column = 1)

txt = StringVar()
screenReturn =  Label(main,width=25, textvariable=txt)
screenReturn.grid(row= 2, column = 1)

testButton = Button(main, text="Test if bissextile", command=bissextile)
testButton.grid(row=3, column=1)

def shutdown():
    global run
    run = False
    main.quit()
main.protocol("WM_DELETE_WINDOW", shutdown)

run=True
while run:
    kInput()
    main.update()
