
# Python code that asks a user how many pizza slices they want.The pizzeria charges Rs 123.00 a slice. if user order even number of slices, 
# price per slice is Rs 120.00. Print the total price depending on how many slices user orders.

a = int(input())
total=0
if(a % 2==0):
    b=120*a
    total+=b
else:
    c=130*a
    total+=c
print(total)
