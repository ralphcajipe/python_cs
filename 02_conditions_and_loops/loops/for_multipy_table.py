"""Print a Multiplication Table"""

# multiplicand x multiplier = product
for multiplicand in range(1, 11):
    for multiplier in range(1, 11):
        product = multiplicand * multiplier
        print(product, end=' ')
    print("")
