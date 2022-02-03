a = ['foo', 'bar', 'baz', 'qux', 'corge']

while a:

    if len(a) < 3:
        continue

    print(a.pop())

print('Done.')
