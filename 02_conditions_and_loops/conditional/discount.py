"""
Program to compute the discount:
Discount is calculated on the input amount. Rate of discount is 5%,
if the amount is less than 1000, and 10% if it is above 10_000.
"""

amount = float(input("Enter amount: "))
discount = 0.0

if amount < 1000:
    discount = amount * 0.05
    print("Discount: %.2f" % discount)
else:
    discount = amount * 0.10
    print("Discount: %.2f" % discount)

net_payable = amount - discount
print("Net payable: %.2f" % net_payable)
