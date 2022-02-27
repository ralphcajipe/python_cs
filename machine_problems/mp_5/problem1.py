l = [63, 52, 10, 42, 32, 17, 60, 45, 47, 39,
     71, 55, 41, 95, 70, 48, 42, 32, 13, 35]

length = len(l)

print("Display LIST", l)

print("AVERAGE", sum(l) / len(l))

print("SMALLEST/LARGEST", min(l), max(l))

l.sort()
print("2nd SMALLEST/LARGEST", l[1], l[-2])

even_count, odd_count = 0, 0
for number in l:
    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("Total number of Even numbers", even_count)
print("Total number of Odd numbers", odd_count)