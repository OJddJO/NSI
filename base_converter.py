def dec2bin(x):
    x = int(x)
    binary = ""
    binRes = 0
    while x!=0:
        binRes = x % 2
        x = x // 2
        binary = str(binRes) + binary
    return binary

def bin2dec(x):
    x = int(x)
    x = str(x)
    decimal = 0
    for i in range(len(x)):
        if int(x[i]) == 1:
            decimal += 2**(len(x)-i-1)
    return decimal

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

def bin2hex(x):
    return dec2hex(bin2dec(x))

def hex2bin(x):
    return dec2bin(hex2dec(x))


def conv():
    try:
        b1 = base1.get()
        b2 = base2.get()
        value = entry1.get()
        if b1 == "Dec" and b2 == "Bin":
            returnedValue.set(str(dec2bin(value)))
        elif b1 == "Bin" and b2 == "Dec":
            returnedValue.set(str(bin2dec(value)))
        elif b1 == "Dec" and b2 == "Hex":
            returnedValue.set(str(dec2hex(value)))
        elif b1 == "Hex" and b2 == "Dec":
            returnedValue.set(str(hex2dec(value)))
        elif b1 == "Bin" and b2 == "Hex":
            returnedValue.set(str(bin2hex(value)))
        elif b1 == "Hex" and b2 == "Bin":
            returnedValue.set(str(hex2bin(value)))
        else:
            returnedValue.set("Please do a convertion")
    except:
        pass


from tkinter import *
from keyboard import *

def kInput():
    if is_pressed('enter'):
        conv()

main = Tk()
main.title("Base Converter")
main.resizable(False, False)

base = ["Dec", "Bin", "Hex"]

entry1 = Entry(main, width=25, justify=CENTER)
entry1.grid(row=0, column=0, padx=5)

base1 = StringVar()
base1.set(base[0])
option1 = OptionMenu(main, base1, *base)
option1.grid(row=0, column=2)


returnedValue = StringVar()
entry2 = Label(main, width=25, textvariable=returnedValue, justify=CENTER)
entry2.config(relief='groove')
entry2.grid(row=0, column=3)

base2 = StringVar()
base2.set(base[1])
option2 = OptionMenu(main, base2, *base)
option2.grid(row=0, column=4)

convert = Button(main, text="Convert", command=conv)
convert.grid(row=1, column=0, columnspan=5)

def shutdown():
    global run
    run = False
    main.quit()
main.protocol("WM_DELETE_WINDOW", shutdown)

run = True

while run:
    main.update()
    kInput()
