
# Python program to convert a list into a nested dictionary of keys

list_1 = [1, 2, 3, 4]
dict_1 = current = {}
for name in list_1:
    current[name] = {}
    current = current[name]
print(dict_1)
