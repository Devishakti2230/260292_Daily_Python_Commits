
#Python program to find the repeated items of a tuple

from collections import Counter
tup=(1,3,4,32,1,1,1,31,32,12,21,2,3)  
for k, v in Counter(tup).items():
    if v > 1:
        print("Repeated: {}".format(k))

        
