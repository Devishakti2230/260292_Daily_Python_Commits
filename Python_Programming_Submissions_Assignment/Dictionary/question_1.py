
# Python script to merge two Python dictionaries

#Function to merge to dictionaries
def Merge(dict1, dict2):
    return(dict2.update(dict1))
dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}
print(Merge(dict2, dict1))
print(dict1)
