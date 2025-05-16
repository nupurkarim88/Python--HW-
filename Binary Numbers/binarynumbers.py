def decimal_to_binary(decimal_num):
    if decimal_num == 0:
        return "0"
    
    binary_string = ""
    while decimal_num > 0:
        remainder = decimal_num % 2
        binary_string = str(remainder) + binary_string
        decimal_num //= 2
    return binary_string

decimal_input = int(input("Enter a decimal number: "))
binary_output = decimal_to_binary(decimal_input)
print(f"The binary representation of {decimal_input} is: {binary_output}")


#This program takes a decimal number as input and returns its binary  as a string. It handles the special case of 0 and uses a while loop to repeatedly divide the number by 2,  the remainder to the binary string until the number becomes 0.
