text = "The quick brown fox jumps over the lazy dog"
mylist = text.split(" ")
print(mylist)

mylist = ['The', 'quick', 'brown',
          'fox', 'jumps', 'over',
          'the', 'lazy', 'dog']

# The length of each value/word in mylist
newlist = [len(x) for x in mylist]
print(newlist)
