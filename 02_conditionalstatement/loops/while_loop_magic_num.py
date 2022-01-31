from random import randint

magic_number = randint(1, 9)

print(magic_number)
attempt = 1

while attempt <= 3:
    guess_number = int(input("Magic Number:"))
    if guess_number == magic_number:
        print("Congrats! You nailed it!")
    else:
        print("Try again!")
    attempt += 1
else:
    print("No more attempts left. Better luck next time!")
