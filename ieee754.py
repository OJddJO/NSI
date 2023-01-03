def ieee754b32ToDec(binary:str):
    binList = []
    for element in binary:
        if element not in ['0', '1']:
            raise ValueError("The binary number must be in binary format")
        else:
            binList.append(int(element))
    if len(binList) != 32:
        raise ValueError("The binary number must be 32 bits long")
    else:
        if binList[0] == 0:
            sign = 1
        else:
            sign = -1
        exponent = binList[1:9]
        mantissa = binList[9:]
        exponent = sum([exponent[i] * 2 ** (7 - i) for i in range(len(exponent))])
        mantissa = sum([mantissa[i] * 2 ** (-(i + 1)) for i in range(len(mantissa))])
        return sign * (1 + mantissa) * 2 ** (exponent - 127)

print(ieee754b32ToDec("11000011010101101100000000000000"))

def ieee754b64ToDec(binary:str):
    binList = []
    for element in binary:
        if element not in ['0', '1']:
            raise ValueError("The binary number must be in binary format")
        else:
            binList.append(int(element))
    if len(binList) != 64:
        raise ValueError("The binary number must be 64 bits long")
    else:
        if binList[0] == 0:
            sign = 1
        else:
            sign = -1
        exponent = binList[1:12]
        mantissa = binList[12:]
        exponent = sum([exponent[i] * 2 ** (10 - i) for i in range(len(exponent))])
        mantissa = sum([mantissa[i] * 2 ** (-(i + 1)) for i in range(len(mantissa))])
        return sign * (1 + mantissa) * 2 ** (exponent - 1023)

print(ieee754b64ToDec("1100000000000000000000000000000000000000000000000000000000000000"))

def decToIeee754b32(number:float):
    if number < 0:
        sign = 1
        number = -number
    else:
        sign = 0
    exponent = 0
    while number >= 2:
        number /= 2
        exponent += 1
    while number < 1:
        number *= 2
        exponent -= 1
    mantissa = number - 1
    exponent += 127
    exponent = bin(exponent)[2:]
    exponent = "0" * (8 - len(exponent)) + exponent
    mantissa = bin(int(mantissa * 2 ** 23))[2:]
    mantissa = mantissa + "0" * (23 - len(mantissa))
    return str(sign) + exponent + mantissa

print(decToIeee754b32(0.5))

def decToIeee754b64(number:float):
    if number < 0:
        sign = 1
        number = -number
    else:
        sign = 0
    exponent = 0
    while number >= 2:
        number /= 2
        exponent += 1
    while number < 1:
        number *= 2
        exponent -= 1
    mantissa = number - 1
    exponent += 1023
    exponent = bin(exponent)[2:]
    exponent = "0" * (11 - len(exponent)) + exponent
    mantissa = bin(int(mantissa * 2 ** 52))[2:]
    mantissa = mantissa + "0" * (52 - len(mantissa))
    return str(sign) + exponent + mantissa