def toString(array):
    string = ""
    for element in array:
        string += str(element)
    return string


def binaryToDec(binary):
    dec = 0
    length = len(binary) - 1
    for i in range(length):
        dec += 2**i * int(binary[length - i])
    print(dec)


binaryToDec("0010")


def decToBinary(dec):
    binary = [0] * 8
    i = 0
    while dec:
        binary[i] = dec % 2
        print(i)
        i = i + 1
        dec = dec // 2

    binary.reverse()
    binary = toString(binary)
    print(binary)

    num = 50000000
    while num:
        print(num, end="   ")
        print(num % 2, end=" ")
        num = num // 2


decToBinary(5)
