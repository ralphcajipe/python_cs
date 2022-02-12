def xyz_diff(str1, str2):
    """
    Returns the first location in which the strings differ.
    If the strings are identical, it should return -1.
    """
    if str1 == str2:
        return -1
    else:
        i = 1
        for str1, str2 in zip(str1, str2):
            if str1 != str2:
                break
            i += 1
        return i


string1 = input("Enter first string:")
string2 = input("Enter second string:")
print(xyz_diff(string1, string2))
