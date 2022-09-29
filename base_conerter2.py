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


def convert():
    if decimal.get() != "":
        binary.set(dec2bin(int(decimal.get())))
        hexadecimal.set(dec2hex(int(decimal.get())))
    elif binary.get() != "":
        decimal.set(bin2dec(int(binary.get())))
        hexadecimal.set(bin2hex(int(binary.get())))
    elif hexadecimal.get() != "":
        decimal.set(hex2dec(int(hexadecimal.get())))
        binary.set(hex2bin(int(hexadecimal.get())))


from tkinter import *

main = Tk()
main.title("Base Converter")
main.resizable(False, False)

txt1 = Label(main, text="Decimal:", width=15)
txt1.grid(row=0, column=0)
decimal = StringVar()
entry1 = Entry(main, width=40, textvariable=decimal, justify=CENTER)
entry1.grid(row=0, column=1)

txt2 = Label(main, text="Binaire:", width=15)
txt2.grid(row=1, column=0)
binary = StringVar()
entry2 = Entry(main, width=40, textvariable=binary, justify=CENTER)
entry2.grid(row=1, column=1)

txt3 = Label(main, text="Hexadecimal:", width=15)
txt3.grid(row=2, column=0)
hexadecimal = StringVar()
entry3 = Entry(main, width=40, textvariable=hexadecimal, justify=CENTER)
entry3.grid(row=2, column=1)


def shutdown():
    global run
    run = False
    main.quit()
main.protocol("WM_DELETE_WINDOW", shutdown)

run = True

while run:
    main.update()
    convert()
