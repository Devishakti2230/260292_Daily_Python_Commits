# Sets

Days = set(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])    
print(Days)    
print(type(Days))    
print("looping through the set elements ... ")    
for i in Days:    
    print(i)   
 

set3 = {}  
print(type(set3))  
set4 = set()  
print(type(set4))  


Months = set(["January","February", "March", "April", "May", "June"])    
print("\nprinting the original set ... ")    
print(months)    
print("\nAdding other months to the set...");    
Months.add("July");    
Months.add ("August");    
print("\nPrinting the modified set...");    
print(Months)    
print("\nlooping through the set elements ... ")    
for i in Months:    
    print(i)  
    
    
months = set(["January","February", "March", "April", "May", "June"])    
print("\nprinting the original set ... ")    
print(months)    
print("\nRemoving some months from the set...");    
months.discard("January");    
months.discard("May");    
print("\nPrinting the modified set...");    
print(months)    
print("\nlooping through the set elements ... ")    
for i in months:    
    print(i)   
    
    
    
Days1 = {"Monday","Tuesday","Wednesday","Thursday", "Sunday"}    
Days2 = {"Friday","Saturday","Sunday"}    
print(Days1|Days2) 


Days1 = {"Monday","Tuesday","Wednesday","Thursday"}    
Days2 = {"Friday","Saturday","Sunday"}    
print(Days1.union(Days2))


Days1 = {"Monday","Tuesday", "Wednesday", "Thursday"}    
Days2 = {"Monday","Tuesday","Sunday", "Friday"}    
print(Days1&Days2)

a = {"Devansh", "bob", "castle"}    
b = {"castle", "dude", "emyway"}    
c = {"fuson", "gaurav", "castle"}       
a.intersection_update(b, c)       
print(a)    

Days1 = {"Monday",  "Tuesday", "Wednesday", "Thursday"}    
Days2 = {"Monday", "Tuesday", "Sunday"}    
print(Days1.difference(Days2))


a = {1,2,3,4,5,6}  
b = {1,2,9,8,10}  
c = a.symmetric_difference(b)  
print(c)  
