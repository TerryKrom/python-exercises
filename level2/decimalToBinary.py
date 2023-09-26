# convert Decimal to binary

num = int(input("Enter a decimal number: "))
binary = bin(num).split('0b')
print(binary[1])