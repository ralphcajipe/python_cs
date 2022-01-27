"""
Machine Problem 2"
The program that you create for this exercise
will begin by reading the cost of a meal ordered at a restaurant from the user.
Then your program will compute the tax and tip for the meal.
Use your local tax rate when computing the amount of tax owing.

Compute the tip as 18 percent of the meal amount (without the tax).
The output from your program should include the tax amount,
the tip amount, and the grand total for the meal including both the tax
and the tip.
Format the output so that all the values are displayed using
two decimal places.
"""

# Initialize the tax and tip for a meal.
taxRate = 0.23  # 23%
tipPercentage = 0.18  # 18%

# Read the cost of a meal ordered from the user
mealAmount = float(input("Please enter the meal \
amount excluding tax: $"))

# Compute the tax, tip, and grant total
tip = mealAmount * tipPercentage
tax = mealAmount * taxRate
grandTotal = mealAmount + tax + tip

# Display output
print("Tax: $%.2f." % tax)
print("Tip: $%.2f." % tip)
print("Grand TOTAL: $%.2f." % grandTotal)
