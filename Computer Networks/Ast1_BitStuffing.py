# Bit stuffing
def Stuff(originalSignal):
    signal = list(originalSignal)
    index = 0
    num_of_Ones = 0  # counting the number of ones
    added_zeroes = 0  # counting the number of bits added/stuffed
    bitStuff_Index = []  # add 0 at these places
    for i in signal:
        index += 1
        if i == '1':
            num_of_Ones += 1
        elif i == '0':
            num_of_Ones = 0
        if num_of_Ones == 5 and originalSignal[index - 6] == '0':
            bitStuff_Index.append(index + added_zeroes)
            added_zeroes += 1
            num_of_Ones = 0
    for i in bitStuff_Index:  # adding 0 to the signal = stuffing
        signal.insert(i, '0')
    return signal
# Bit un-stuffing


def unStuff(stuffedSignal):
    signal = list(stuffedSignal)
    index = 0
    num_of_Ones = 0  # counting the number of ones
    added_zeroes = 0  # counting the number of bits added/stuffed
    bitUnstuff_Index = []  # remove 0 from these places
    for i in signal:
        index += 1
        if i == '1':
            num_of_Ones += 1
        elif i == '0':
            num_of_Ones = 0
        if num_of_Ones == 5:
            bitUnstuff_Index.append(index + added_zeroes)
            added_zeroes -= 1
            num_of_Ones = 0
    for i in bitUnstuff_Index:  # removing 0 from the signal = un-stuffing
        signal.pop(i)
    return signal


# Main function
print("\nDevanshu Gupta [21BCE0597]\n")
originalSignal = input("Enter the input signal: ")
stuffedSignal = Stuff(originalSignal)
print("       Stuffed Signal = " + "".join([a for a in stuffedSignal]))
unstuffedSignal = unStuff(stuffedSignal)
print("    Un-stuffed Signal = " + "".join([a for a in unstuffedSignal]))
print("\nDevanshu Gupta [21BCE0597]\n")