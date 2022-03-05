fo = open("read_test.txt", "r+")
"""
Here passed parameter is the number of bytes to be read from the opend file. 
This method starts reading from the beginning of the file and if count is 
missing then it tries to read as much as possible, may be until the end of file
"""
read_string = fo.read(11)
print("Read string is:", read_string)
fo.close()