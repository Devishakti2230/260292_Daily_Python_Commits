# For loop
list = [1,2,3,4,5,6,7,8,9,10]  
n = 5  
for i in list:  
    c = n*i  
    print(c)  

    
n = int(input("Enter the number "))  
for i in range(1,11):  
    c = n*i  
    print(n,"*",i,"=",c)  
 

rows = int(input("Enter the rows"))  
for i in range(0,rows+1):  
    for j in range(i):  
        print(i,end = '')  
    print()  
 

for i in range(0,5):    
    print(i)    
    break;    
else:print("for loop is exhausted");    
print("The loop is broken due to break statement...came out of the loop")  

#While Loop

i = 0  
str1 = 'STEPIN'  
  
while i < len(str1):   
    if str1[i] == 't':   
        i += 1  
        break  
    print('Current Letter :', str1[i])   
    i += 1  
 

i=1    
number=0    
b=9    
number = int(input("Enter the number:"))    
while i<=10:    
    print("%d X %d = %d \n"%(number,i,number*i))    
    i = i+1   
    
    
i=1    
while(i<=5):    
    print(i)    
    i=i+1    
    if(i==3):    
        break   
else:  
    print("The while loop exhausted")  
