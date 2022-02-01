credit = input("How many credits units you have taken: ")
credit = int(credit)

if credit >= 1 and credit < 23:
    print("You are a freshman...")
elif credit > 23 and credit <= 53:
    print("You are a sophomore...")
elif credit >= 54 and credit <= 83:
    print("You are juniors...")
elif credit >= 84:
    print("You are seniors...")
else:
    print("Entry is invalid...")
