"""
def multiply(a,b):
    c=a*b
    #print(c)
    return c
a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
z=multiply(a,b)
print("the value of z is:",z)


def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)
n=int(input("Input the value of n:"))
c=fact(n)
print(c)

def var(a):
    print(a)
    print(b)
a=20
b=30
var(a)

def var(a):
    c=20
    print(a,c)

a=20
b=30
print(a)
print(b)
print(c)
var(a)


def net(n):
    print(n)
    net(n-1)
n=50
net(n)
"""
def fibo(n):
   if n <= 1:
       return n
   else:
       return(fibo(n-1) + fibo(n-2))
n = int(input("enter the value of n :"))

if n <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(n):
       print(fibo(i))


