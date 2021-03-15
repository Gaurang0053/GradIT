
"""
def Divisors(n):
    i = 1
    while i <= n:
        if (n % i == 0):
            print (i)
        i = i + 1
print
"The divisors of are: ",Divisors(50)

lst=map(int,input().split())
print(lst)
"""

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
if x > y:
    smaller = y
else:
    smaller = x
for i in range(1,smaller + 1):
    if((x % i == 0) and (y % i == 0)):
        hcf = i
print("The H.C.F. of", x,"and", y,"is", hcf)






