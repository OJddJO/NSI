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

