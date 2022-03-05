"""
The close() method of a file object flushes any unwritten information and
closes the file object, after which no more writing can be done.
Python automatically closes a file when the reference object of a file is
reassigned to another file. It is a good practice to use the close() method
to close a file.
"""
f = open("close_test.txt")
print("Name of file:", f.name)
f.close()