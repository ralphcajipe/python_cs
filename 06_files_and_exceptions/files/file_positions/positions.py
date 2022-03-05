fo = open("positions_test.txt", "r+")

read_string = fo.read(10)
print("Read String is:", read_string)

position = fo.tell()
print("Current file position:", position)

position = fo.seek(0, 0)
read_string2 = fo.read(10)
print("Again read String is:", read_string2)

fo.close()
