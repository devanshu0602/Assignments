# converting an Octet to Decimal
def toDecimal(octet):
    total = 0
    exponent = 7
    for i in range(0,8):
        bit = int(octet[i])
        bit = bit * (2 ** exponent)
        total = total + bit
        exponent -= 1
    return total

# Main function
print("Devanshu Gupta [21BCE0597]\n")
bin_IP = input("Enter the IP: ")
if len(bin_IP) != 32:
    padding_count = 32 - len(bin_IP)
    padding = '0' * padding_count
    bin_IP = padding + bin_IP
octet1 = bin_IP[0:8]
octet2 = bin_IP[8:16]
octet3 = bin_IP[16:24]
octet4 = bin_IP[24:32]
dec_octet1 = toDecimal(octet1)
dec_octet2 = toDecimal(octet2)
dec_octet3 = toDecimal(octet3)
dec_octet4 = toDecimal(octet4)
dec_IP = str(dec_octet1) + "." + str(dec_octet2) + "." + str(dec_octet3) + "." + str(dec_octet4)
print(octet1, octet2, octet3, octet4, "---Decimal--->", dec_IP)
print("\nDevanshu Gupta [21BCE0597]\n")