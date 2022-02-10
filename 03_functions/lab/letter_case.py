def string_test(s):
    """Count the number of uppercase and lowercase in a string."""
    d = {"UPPER_CASE": 0, "LOWER_CASE": 0}
    for c in s:
        if c.isupper():
            d["UPPER_CASE"] += 1
        elif c.islower():
            d["LOWER_CASE"] += 1
        else:
            pass

    print("Original String: ", s)
    print("Upper case count ", d["UPPER_CASE"])
    print("Lower case count ", d["LOWER_CASE"])


string_test("RALph caJIPE")
