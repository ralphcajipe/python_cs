temp = float(input("Enter a temperature: "))

if temp < -273.15:
    print("Temperature is invalid because it is below absolute zero.")
elif temp == -273.15:
    print("Temperature is absolute 0.")
elif temp > -273.15 and temp < 0:
    print("Temperature is below freezing.")
elif temp == 0:
    print("Temperature is at the freezing point.")
elif temp > 0  and temp < 100:
    print("Temperature is in the normal range.")
elif temp == 100:
    print("Temperature is at the boiling point.")
else:
    print("Temperature is above the boiling point.")
