# Python also allows you to create your own exceptions by deriving classes
# from the standard built-in exceptions

class NetworkError(RuntimeError):
    """A child class is created that is subclassed from
    parent class RuntimeError."""

    # This is useful when you need to display more specific information when an
    # exception is caught.
    def __init__(self, arg):
        self.arg = arg


# In the try block, the user-defined exception is raised and caught in the
# except block. The variable `e` is used to create an instance of the class
# Networkerror
try:
    raise NetworkError("Bad hostname")
except NetworkError as e:
    print(e.arg)
