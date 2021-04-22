
num=input()
if(num.isnumeric()):
  print("real")
elif(num==0):
    print("Zero")
elif(isinstance(num, int) == True):
    print("Integer")
elif(isinstance(num, float) == True):
    print("Float")
elif(isinstance(num, complex)==True):
    print("Complex")
else:
    print("String")
