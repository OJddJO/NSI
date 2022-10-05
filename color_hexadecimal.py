def dec2hex(x):
    x = int(x)
    hex = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    hexadecimal = ''
    res = 0
    while x != 0:
        res = x % 16
        x //= 16
        hexadecimal = hex[res] + hexadecimal
    if hexadecimal == "":
        hexadecimal = "00"
    if len(hexadecimal) == 1:
        hexadecimal = "0"+hexadecimal
    return hexadecimal

def hex2dec(x):
    x = str(x)[::-1]
    hex = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    decimal = 0
    for i in range(len(x)):
        decimal += hex.index(x[i])*(16**i)
    return decimal

def convert(t):
    try:
        if t == "hex":
            r.set(hex2dec(Rhex.get()))
            g.set(hex2dec(Ghex.get()))
            b.set(hex2dec(Bhex.get()))
        elif t == "dec":
            Rhex.set(dec2hex(r.get()))
            Ghex.set(dec2hex(g.get()))
            Bhex.set(dec2hex(b.get()))
    except:
        pass

def correction(t):
    global color
    if int(r.get()) > 255:
        r.set("255")
    if int(g.get()) > 255:
        g.set("255")
    if int(b.get()) > 255:
        b.set("255")
    
    if r.get() == "":
        r.set("0")
    if g.get() == "":
        g.set("0")
    if b.get() == "":
        b.set("0")

    try:
        col = f"#{Rhex.get()}{Ghex.get()}{Bhex.get()}"
        color.config(bg=col)
    except Exception as e:
        print(e)
    
    convert(t) 


from tkinter import *

main = Tk()
main.resizable(False, False)

r = StringVar(value="0")
g = StringVar(value="0")
b = StringVar(value="0")

Rhex = StringVar(value="00")
Ghex = StringVar(value="00")
Bhex = StringVar(value="00")

hexTxt = Label(main, text="Hex", justify=CENTER)
decTxt = Label(main, text="Dec", justify=CENTER)
hexTxt.grid(row=0, column=2)
decTxt.grid(row=0, column=1)

redTxt = Label(main, text="Red: ")
redDec = Entry(main, textvariable=r, justify=CENTER)
redHex = Entry(main, textvariable=Rhex, justify=CENTER)
redTxt.grid(row=1, column=0)
redDec.grid(row=1, column=1)
redHex.grid(row=1, column=2)

greenTxt = Label(main, text="Green: ")
greenDec = Entry(main, textvariable=g, justify=CENTER)
greenHex = Entry(main, textvariable=Ghex, justify=CENTER)
greenTxt.grid(row=2, column=0)
greenDec.grid(row=2, column=1)
greenHex.grid(row=2, column=2)

blueTxt = Label(main, text="Blue: ")
blueDec = Entry(main, textvariable=b, justify=CENTER)
blueHex = Entry(main, textvariable=Bhex, justify=CENTER)
blueTxt.grid(row=3, column=0)
blueDec.grid(row=3, column=1)
blueHex.grid(row=3, column=2)

color = Canvas(main)
color.grid(row=4, column=0, columnspan=3)

#Convert value
r.trace_add("write", lambda name, index, mode, type="dec": correction(type))
g.trace_add("write", lambda name, index, mode, type="dec": correction(type))
b.trace_add("write", lambda name, index, mode, type="dec": correction(type))
Rhex.trace_add("write", lambda name, index, mode, type="hex": correction(type))
Ghex.trace_add("write", lambda name, index, mode, type="hex": correction(type))
Bhex.trace_add("write", lambda name, index, mode, type="hex": correction(type))

def shutdown():
    global run
    run = False
    main.quit()
main.protocol("WM_DELETE_WINDOW", shutdown)

run = True
while run:
    main.update()
    for element in main.children:
        if element in [Label, Entry, StringVar]:
            element.update()
