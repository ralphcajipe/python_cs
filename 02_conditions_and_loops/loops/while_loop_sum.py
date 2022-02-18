# Program to add natural numbers
# numbers up to
# sum = 1+2+3+...+number

# To take user input,
# number = int(input("Enter number: "))
number = 10

# Initialize the sum and counter or increment
the_sum = 0
i = 1

while i <= number:
    the_sum += i
    i += 1  # update counter or increment


print(f"The sum is {the_sum}")