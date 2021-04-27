# List

L1 = ["John", 102, "USA"]    
L2 = [1, 2, 3, 4, 5, 6]   
print(type(L1))  
print(type(L2))  


a = [1, 2,"Peter", 4.50,"Ricky",5, 6]  
b = [1, 2,"Peter", 4.50,"Ricky",5, 6]  
a == b  


list = [1,2,3,4,5,6,7]  
print(list[0])  
print(list[1])  
print(list[2])  
print(list[3])  
# Slicing the elements  
print(list[0:6])  
# By default the index value is 0 so its starts from the 0th element and go for index -1.  
print(list[:])  
print(list[2:5])  
print(list[1:6:2])  


list = [1, 2, 3, 4, 5, 6]     
print(list)     
# It will assign value to the value to the second index   
list[2] = 10   
print(list)    
# Adding multiple-element   
list[1:3] = [89, 78]     
print(list)   
# It will add value at the end of the list  
list[-1] = 25  
print(list)  


list = [0,1,2,3,4]     
print("printing original list: ");    
for i in list:    
    print(i,end=" ")    
list.remove(2)    
print("\nprinting the list after the removal of first element...")    
for i in list:    
    print(i,end=" ")  
    
    
list1 = [1,2,3,4,5,6]  
list2 = [7,8,9,2,10]  
for x in list1:  
    for y in list2:  
        if x == y:  
            print("The common element is:",x)  
            
            
