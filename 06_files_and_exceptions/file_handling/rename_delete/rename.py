import os

try:
    # The rename() method takes two arguments,
    # the current filename and the new filename
    os.rename("rename_test2.txt", "rename_test.txt")
except FileNotFoundError:
    print(f"The file cannot be found.")
else:
    print("Rename successful.")