a = ['foo', 'bar', 'baz', 'qux', 'corge']

while a:

    if len(a) < 3:
        break

    print(a.pop())

print('Done.')
