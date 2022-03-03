while True:
    try:
        addend1 = int(input("Enter first addend:" ))
        addend2 = int(input("Enter second addend:" ))
    except ValueError:
        print("\tThat is not an integer number.")
        print()
    else:
        print(f"The sum is {addend1+addend2}")
