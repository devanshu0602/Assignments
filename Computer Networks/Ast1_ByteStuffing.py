# Global variable
byteStuff_index = []

# Byte stuffing
def Stuff(original_signal):
    signal = list(original_signal)
    # create a list of special characters
    special_char = ['#', '/', '@', '&', '*', '%', '$']
    index = 0
    # Counting the number of times stuffing occured
    added_symbols = 0
    global byteStuff_index
    for i in signal:
        # if the character is a special character 
        # then add its index to the list
        if i in special_char:
            byteStuff_index.append(index + added_symbols)
            added_symbols += 1  # increment the number of stuffings
        index += 1
    for i in byteStuff_index:
        # insert the escape character wherever required
        signal.insert(i, '/') 
    return signal


# Byte unstuffing
def unStuff(stuffed_signal):
    signal = list(stuffed_signal)
    added_symbols = 0
    global byteStuff_index
    for i in byteStuff_index:
        # remove all the escape characters
        # to make it original again
        signal.pop(i + added_symbols)
        added_symbols -= 1
    return signal


# Main function
print("\nDevanshu Gupta [21BCE0597]\n")
original_signal = input("Enter the input signal: ")
stuffed_signal = Stuff(original_signal)
print("       Stuffed signal = " + "".join([a for a in stuffed_signal]))
unstuffed_signal = unStuff(stuffed_signal)
print("    Un-stuffed signal = " + "".join([a for a in unstuffed_signal]))
print("\nDevanshu Gupta [21BCE0597]\n")