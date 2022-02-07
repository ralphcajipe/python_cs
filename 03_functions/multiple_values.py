# function that returns multiples values
# x = de-bf / ad - bc
# y = af-ce / ad - bc

def solve(a, b, c, d, e, f):
    x = (d * e - b * f) / (a * d - b * c)
    y = (a * f - c * e) / (a * d - b * c)
    return [x, y]
    # return x, y


xsol, ysol = solve(2, 3, 4, 1, 2, 5)
print("x = ", xsol, " y = ", ysol)
