def dec2hex(x):
    x = int(x)
    hex = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    hexadecimal = ''
    res = 0
    while x != 0:
        res = x % 16
        x //= 16
        hexadecimal = hex[res] + hexadecimal
    return hexadecimal

def hex2dec(x):
    x = str(x)[::-1]
    hex = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    decimal = 0
    for i in range(len(x)):
        decimal += hex.index(x[i])*(16**i)
    return decimal

def convert(type):
    if type == "hex":
        R.set(hex2dec())



from tkinter import *

main = Tk()
main.resizable(False, False)

R = StringVar(value="0")
G = StringVar(value="0")
B = StringVar(value="0")

Rhex = StringVar(value="00")
Ghex = StringVar(value="00")
Bhex = StringVar(value="00")

hexTxt = Label(main, text="Hex", justify=CENTER)
decTxt = Label(main, text="Dec", justify=CENTER)
hexTxt.grid(row=0, column=1)
decTxt.grid(row=0, column=2)

redTxt = Label(main, text="Red: ")
redDec = Entry(main, textvariable=R, justify=CENTER)
redHex = Entry(main, textvariable=Rhex, justify=CENTER)
redTxt.grid(row=1, column=0)
redDec.grid(row=1, column=1)
redHex.grid(row=1, column=2)

greenTxt = Label(main, text="Green: ")
greenDec = Entry(main, textvariable=G, justify=CENTER)
greenHex = Entry(main, textvariable=Ghex, justify=CENTER)
greenTxt.grid(row=2, column=0)
greenDec.grid(row=2, column=1)
greenHex.grid(row=2, column=2)

blueTxt = Label(main, text="Blue: ")
blueDec = Entry(main, textvariable=B, justify=CENTER)
blueHex = Entry(main, textvariable=Bhex, justify=CENTER)
blueTxt.grid(row=3, column=0)
blueDec.grid(row=3, column=1)
blueHex.grid(row=3, column=2)

#Convert value
R.trace_add("write", lambda name, index, mode, type="dec", value=R.get(), col="red" : convert(type, value, col))
G.trace_add("write", lambda name, index, mode, type="dec", value=G.get(), col="green" : convert(type, value, col))
B.trace_add("write", lambda name, index, mode, type="dec", value=B.get(), col="blue" : convert(type, value, col))
Rhex.trace_add("write", lambda name, index, mode, type="hex", value=Rhex.get(), col="red" : convert(type, value, col))
Ghex.trace_add("write", lambda name, index, mode, type="hex", value=Ghex.get(), col="green" : convert(type, value, col))
Bhex.trace_add("write", lambda name, index, mode, type="hex", value=Bhex.get(), col="blue" : convert(type, value, col))

main.mainloop()
