"""
A small deposit is added to drink containers
to encourage people to recycle them.

Suppose drink containers holding one liter or less have a $0.10 deposit,
and drink containers holding more than one liter have a $0.25 deposit.

Write a program that reads the number of containers
of each size from the user.

Your program should continue by computing and displaying the refund that
will be received for returning those containers.

Format the output so that it includes a dollar sign and
two digits to the right of the decimal point.

The %.2f format specifier indicates that a value should be formatted as
a floating-point number with 2 digits to the right of the decimal point.
"""

# Value of deposit for a certain collection of returned containers
oneLitreOrLess = 0.10
moreThanOneLitre = 0.25

# Input
one_less = int(input("How many bottles have one litre or less?: "))
more = int(input("How many bottles have more than one litre?: "))

# Compute refund for returning
refund = (one_less * oneLitreOrLess) + (more * moreThanOneLitre)

# Display refund output
print("\nThe refund for returning these containers is $%.2f." % refund)
