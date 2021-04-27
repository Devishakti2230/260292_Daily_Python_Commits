# Tuple

T1 = (101, "Peter", 22)    
T2 = ("Apple", "Banana", "Orange")     
T3 = 10,20,30,40,50  
print(type(T1))  
print(type(T2))  
print(type(T3))  


tuple1 = (10, 20, 30, 40, 50, 60)    
print(tuple1)    
count = 0    
for i in tuple1:    
    print("tuple1[%d] = %d"%(count, i))   
    count = count+1  
    
    
tup = (1,2,3,4,5,6,7)  
print(tup[0])  
print(tup[1])  
print(tup[2])  
# It will give the IndexError  
print(tup[8])  


tuple1 = (1, 2, 3, 4, 5)    
print(tuple1[-1])    
print(tuple1[-4])    
print(tuple1[-3:-1])  
print(tuple1[:-1])  
print(tuple1[-2:])  


tuple1 = (1, 2, 3, 4, 5, 6)    
print(tuple1)    
del tuple1[0]    
print(tuple1)    
del tuple1    
print(tuple1)    
