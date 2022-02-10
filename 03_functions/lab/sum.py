def get_sum(numbers):
    """Get sum of a list of numbers."""
    total = 0
    for number in numbers:
        total += number
    return total


print(get_sum((1, 2, 3, 4, 5)))
