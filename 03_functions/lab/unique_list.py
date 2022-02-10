def unique_list(given_list):
    """Get the unique values in a given list."""
    result = []
    for unique in given_list:
        if unique not in result:
            result.append(unique)
    return result


print(unique_list([1, 2, 3, 4, 4, 3, 2, 3, 4, 6]))
