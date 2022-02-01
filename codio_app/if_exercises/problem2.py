# Temperature conversion
temp = float(input("Enter a temperature: "))
unit = input("Enter C - Celsius; Enter F - Fahrenheit: ")

if unit == 'C':
    newTemp = 9 / 5 * temp + 32
    print("Temperature from Celsius to Fahrenheit is:", newTemp)
elif unit == 'F':
    newTemp = 9 / 5 * (temp - 32)
    print("Temperature from Fahrenheit to Celsius is:", newTemp)
else:
    print("Entry is invalid...")
