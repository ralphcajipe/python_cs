class Number:
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

    def __add__(self, o):
        if isinstance(o, Number):
            self.value += o.value
        elif isinstance(o, int):
            self.value += o
        else:
            raise ValueError
        return self

    def __sub__(self, o):
        if isinstance(o, Number):
            self.value -= o.value
        elif isinstance(o, int):
            self.value -= o
        else:
            raise ValueError
        return self


n = Number('MCMI')
m = Number(5)
print(n.asRoman())
n += m
print(n.asRoman())
m = 4
n -= m
print(n.asRoman())
