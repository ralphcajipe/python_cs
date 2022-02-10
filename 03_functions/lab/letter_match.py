def count_matches(string1, string2):
    """Count the number of character match in a pair of string."""
    set_string1 = set(string1)
    set_string2 = set(string2)

    # & is intersection operator
    # returns a set that contains the similarity between two or more sets.
    matches = set_string1 & set_string2

    print("Matches:", len(matches))


count_matches('ralph', 'apple')
