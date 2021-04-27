#String

str = "HELLO"  
print(str[0])  
print(str[1])  
print(str[2])  
print(str[3])  
print(str[4])  
# It returns the IndexError because 6th index doesn't exist  
print(str[6])  


str = 'JAVATPOINT'  
print(str[-1])  
print(str[-3])  
print(str[-2:])  
print(str[-4:-1])  
print(str[-7:-2])  
# Reversing the given string  
print(str[::-1])  
print(str[-12])  


str = "Hello"     
str1 = " world"    
print(str*3) # prints HelloHelloHello    
print(str+str1)# prints Hello world     
print(str[4]) # prints o                
print(str[2:4]); # prints ll                    
print('w' in str) # prints false as w is not present in str    
print('wo' not in str1) # prints false as wo is present in str1.     
print(r'C://python37') # prints C://python37 as it is written    
print("The string str : %s"%(str)) # prints The string str : Hello     




print("{} and {} both are the best friend".format("Devansh","Abhishek"))  
print("{1} and {0} best players ".format("Virat","Rohit"))  
print("{a},{b},{c}".format(a = "James", b = "Peter", c = "Ricky"))  



print(r"C:\\Users\\DEVANSH SHARMA\\Python32")  
