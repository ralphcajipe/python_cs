prompt = "Enter a number (negative to stop):"

nums = []

while True:
    num = int(input(prompt))

    if num < 0:
        break

    nums.append(num)

sum_is = sum(nums)
print("Sum is", sum_is)
