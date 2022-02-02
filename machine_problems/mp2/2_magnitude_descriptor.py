m = float(input("Enter an earthquake magnitude:"))

if m < 2.0:
    descriptor = "Micro"
elif m >= 2.0 and m < 3.0:
    descriptor = "Very minor"
elif m >= 3.0 and m < 4.0:
    descriptor = "Minor"
elif m >= 4.0 and m < 5.0:
    descriptor = "Light"
elif m >= 5.0 and m < 6.0:
    descriptor = "Moderate"
elif m >= 6.0 and m < 7.0:
    descriptor = "Strong"
elif m >= 7.0 and m < 8.0:
    descriptor = "Major"
elif m >= 8.0 and m < 10.0:
    descriptor = "Great"
else:
    descriptor = "Meteoric"

print(f"This earthquake is classified as {descriptor}")
