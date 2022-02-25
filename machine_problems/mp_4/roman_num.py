import sys

MAX_VALUE_INT = 5000
MAX_VALUE_STR = "MMMMM"


class Number:
    """Accepts integer as input and display
    the equivalent roman numeral and vice-versa.
    """

    control = [
        (1000, 'M', 1),
        (900, 'CM', 2),
        (500, 'D', 1),
        (400, 'CD', 2),
        (100, 'C', 1),
        (90, 'XC', 2),
        (50, 'L', 1),
        (40, 'XL', 2),
        (10, 'X', 1),
        (9, 'IX', 2),
        (5, 'V', 1),
        (4, 'IV', 2),
        (1, 'I', 1)]

    def __init__(self, value):
        if isinstance(value, int):
            self.value = value
        elif value.isdigit():
            self.value = int(value)
        else:
            self.value = self._toInteger(value)

    def asInteger(self):
        return self.value

    def asRoman(self):
        return self.toRoman(self.value)

    def toRoman(self, num):
        if num == 0:
            return ''
        for v, c, _ in Number.control:
            if num >= v:
                return c + self.toRoman(num - v)

    def _toInteger(self, num):
        result, offset = 0, 0
        for c, r, l in Number.control:
            while num[offset:].startswith(r):
                result += c
                offset += l
        return result


# Main Menu
def main():
    print("\nMENU")
    print("[1] Convert an Integer to a Roman Numeral")
    print("[2] convert a Roman Numeral to an Integer")
    print("[3] exit")


while True:
    main()
    choice = eval(input("\nEnter your choice: "))

    if choice == 1:
        user_input = eval(input("Enter Integer:"))
        if int(user_input) > MAX_VALUE_INT:
            print("MAX VALUE is 5000. Try lower than that.")
        else:
            num_obj = Number(user_input)
            print("Output in roman numeral is", num_obj.asRoman())
            # After output, return to Menu

    elif choice == 2:
        user_input = str(input("Enter Roman Numeral:"))
        if MAX_VALUE_STR in str(user_input):
            print("MAX VALUE is MMMMM. Try lower than that.")
        else:
            roman_obj = Number(user_input.upper())
            print("Output in Integer is", roman_obj.asInteger())
            # After output, return to Menu

    elif choice == 3:
        sys.exit()