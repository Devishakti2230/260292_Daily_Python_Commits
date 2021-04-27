# Write a Python program to find the second smallest number in a list

def find_second_smallest(list_1):
    length = len(list1)
    list_1.sort()
    print("Second Smallest element is:", list_1[1])
list_1=[12, 45, 2, 41, 31, 10]
Largest = find_second_smallest(list_1)
