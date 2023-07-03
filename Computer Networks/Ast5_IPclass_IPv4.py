# find class of binary IP
def findClassBinary(ip):
    if ip[0] == '0':
        return 'A'
    elif ip[0:2] == '10':
        return 'B'
    elif ip[0:3] == '110':
        return 'C'
    elif ip[0:4] == '1110':
        return 'D'
    elif ip[0:4] == '1111':
        return 'E'
    
# find class of Decimal-dotted IP
def findClassDec(ip):
    first_octet = ip[0:3]
    if int(first_octet) >= 0 and int(first_octet) <= 127:
        return 'A'
    elif int(first_octet) >= 128 and int(first_octet) <= 191:
        return 'B'
    elif int(first_octet) >= 192 and int(first_octet) <= 223:
        return 'C'
    elif int(first_octet) >= 224 and int(first_octet) <= 239:
        return 'D'
    elif int(first_octet) >= 240 and int(first_octet) <= 255:
        return 'E'

# Main function
print("Devanshu Gupta [21BCE0597]\n")
print("Enter your choice:")
choice = int(input("1. Binary notation\n2. Dotted-Decimal notation\n"))
IP_input = input("\nEnter the IP: ")
if choice == 1:
    class_of_IP = findClassBinary(IP_input)
    print("IP belongs to", class_of_IP)
elif choice == 2:
    class_of_IP = findClassDec(IP_input)
    print("IP belongs to", class_of_IP)
else:
    print("Invalid choice.")
print("\nDevanshu Gupta [21BCE0597]\n")