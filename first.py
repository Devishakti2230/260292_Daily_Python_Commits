# First Program
print("Welcome to StepIn Program!")

# Second Program
def add():
    a = 20
    b = 30
    c = a + b
    print("The sum is:", c)
add()

# Third Program
x = 101
def mainFunction():
    global x
    print(x)
    x = 'Welcome To StepIn Program !'
    print(x)
mainFunction()
print(x)

# Fourth Program
a = int(input("Enter a? "));
b = int(input("Enter b? "));
c = int(input("Enter c? "));
if a > b and a > c:
    print("a is largest");
if b > a and b > c:
    print("b is largest");
if c > a and c > b:
    print("c is largest");

# Fifth Program
list = [10,30,23,43,65,12]
sum = 0
for i in list:
    sum = sum+i
print("The sum is:",sum)

# sixth program
x = lambda a:a+10
print(x)
print("sum = ",x(20))
