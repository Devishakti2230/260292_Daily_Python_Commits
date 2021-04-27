
# Change the position of every n-th value with the (n+1)th in a list

from itertools import zip_longest, chain, tee
def replace2copy(list_1):
    list_2, list_3 = tee(iter(list_1), 2)
    return list(chain.from_iterable(zip_longest(list_1[1::2], list_1[::2])))
list_4 = [0,1,2,3,4,5]
print(replace2copy(list_4))
