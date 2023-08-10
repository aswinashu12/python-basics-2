def sum(x,y):
     return x+y
def difference(x,y):
     return x-y
def mulltiply(x,y):
     return x*y
def divide(x,y):
     return x/y
n1=int(input("enter the first number"))
n2=int(input("enter the second number"))
select=int(input("select operations from 1,2,3,4:"))

# 1: for sum
# 2: for difference
# 3: for multiply
# 4: for divide
if select==1:
     print(sum(n1,n2))
elif select==2:
     print(difference(n1,n2))
elif select==3:
     print(multiply(n1,n2))
elif select==4:
     print(divide(n1,n2))
else:
     print("invalid selection")


