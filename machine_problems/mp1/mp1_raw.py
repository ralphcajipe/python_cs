########################################################
#  Declare your variables here
#  Erase the variable before submitting your work
########################################################

# Value of deposit for a certain collection of returned containers
# 0.10
# 0.25

# Input:
oneLitreOrLess = int(input("\nHow many bottles have one litre or less?: "))
moreThanOneLitre = int(input("How many bottles have more than one litre?: "))

########################################################
# Enter your code below
########################################################

# Compute refund of returned containers
refund = (oneLitreOrLess * 0.10) + (moreThanOneLitre * 0.25)

# Display refund output
print("\nThe refund for returning these containers is $%.2f." % refund)
