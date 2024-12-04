#Adam Dietz
#Conversion Functions
#Decimal to Binary
def dec_to_bi(dec: int):
    #Base case
    if dec == 0:
        return '0'
    #List to hold values
    binary = []
    #Loop till decimal is equal to zero
    while dec>0:
        #Add the modulus of the decimal to the front of the list
        binary.insert(0, str(dec%2))
        #Floor division to progress through the decimal
        dec = dec // 2
    #Return the joined list as a string
    return ''.join(binary)
#Decimal to Hexadecimal
def dec_to_hex(dec: int):
    #Conversion table
    table = {0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',
             9:'9',10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
    #String hexadecimal
    hexadecimal = ''
    #Loop till the decimal is zero
    while dec>0:
        #Conjugate the table value of the modulus with hexadecimal
        hexadecimal = table[dec%16] + hexadecimal
        #Progress through the decimal
        dec = dec // 16
    #Return the hexadeciaml string
    return hexadecimal
#Binary to Decimal
def bi_to_dec(binary: str):
    #Use the parameters of the int function to convert binary to decimal
    return int(binary, 2)
#Binary to Hexadecimal 
def bi_to_hex(binary: str):
    #Call the binary to decimal function and decimal to hexadecimal function to convert
    return dec_to_hex(bi_to_dec(binary))
#Hexadecimal to Decimal
def hex_to_dec(hexadecimal: str):
    #Use the int function to convert hexadecimal to decimal
    return int(hexadecimal,16)
#Hexadecimal to Binary
def hex_to_bi(hexadecimal: str):
    #First convert to decimal then convert to binary
    return dec_to_bi(hex_to_dec(hexadecimal))
#Binary Addition
def binary_adder(b1: str, b2: str):
    #Convert both to decimal add them then convert back to binary
    return dec_to_bi(bi_to_dec(b1) + bi_to_dec(b2))


#Loop Condition
g = 1
while g == 1:
    #Welcome Message and Options
    print("Welcome to the Number System Converter and Binary Adder!")
    print("What would you like to do today?")
    print("1: Decimal to Binary")
    print("2: Decimal to Hexadecimal")
    print("3: Binary to Decimal")
    print("4: Binary to Hexadecimal")
    print("5: Hexadecimal to Decimal")
    print("6: Hexadecimal to Binary")
    print("7: Binary Adder")
    print("8: Quit")
    #Loop till input is an integer
    while True:
        try:
            c = int(input("Enter your choice: "))
            break
        except:
            print("Invalid option!")
    #Exit
    if c == 8:
        g = 0
    #Decimal to Binary
    elif c == 1:
        while True:
            try:
                d = int(input("Enter the decimal number: "))
                break
            except:
                print("Invalid Input")
        print("Binary: " + dec_to_bi(d))
    #Decimal to Hexadecimal
    elif c == 2:
        while True:
            try:
                d = int(input("Enter the decimal number: "))
                break
            except:
                print("Invalid Input")
        print("Hexadecimal: " + dec_to_hex(d))
    #Binary to Decimal
    elif c == 3:
        d = str(input("Enter the binary number: "))
        print("Decimal: " + str(bi_to_dec(d)))
    #Binary to Hexadecimal
    elif c == 4:
        d = str(input("Enter the binary number: "))
        print("Hexadecimal: " + bi_to_hex(d))
    #Hexadecimal to Decimal
    elif c == 5:
        d = str(input("Enter the hexadecimal number: "))
        print("Decimal: " + str(hex_to_dec(d)))
    #Hexadecimal to Binary
    elif c == 6:
        d = str(input("Enter the hexadecimal number: "))
        print("Binary: " + hex_to_bi(d))
    #Binary Adder
    elif c == 7:
        b1 = str(input("Enter the first binary number: "))
        b2 = str(input("Enter the second binary number: "))
        print(b1 + " + " + b2 + " = " + binary_adder(b1,b2))
    #Continue prompt
    b = input("Continue? Y/N: ")
    if(b == 'N' or b == 'n'):
        g = 0

