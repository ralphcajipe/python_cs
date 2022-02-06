num = int(input("Enter a numbr(positive): "))

odd_sum = 0

while num > 0:
    remainder = num % 10
    if remainder % 2 != 0:
        odd_sum += remainder
    num = int(num / 10)

print(f"the AnSer is {odd_sum}")
