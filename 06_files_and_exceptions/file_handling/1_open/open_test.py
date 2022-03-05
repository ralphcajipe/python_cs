f = open("open_test.txt")
# Returns True if file is closed, false otherwise.
print("Closed (True) or not (False):", f.closed)
# In this case, the file is open, so ouput is False.

# If we try to close the file, it results to True
f.close()
print("Closed (True) or not (False):", f.closed)