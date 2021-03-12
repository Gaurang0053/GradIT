"""
n=int(input("enter the value of n:"))
f=1
while n:
     f=f*n
     n=n-1
print("the factorial value is ",f)


n = int(input("How many terms? "))
n1, n2 = 0, 1
c = 0

if n <= 0:
   print("Please enter a positive integer")
elif n == 1:
   print("Fibonacci sequence upto",n,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while c < n:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       c += 1
       """

n = int(input("Enter the number of rows"))
for i in range(0,n):
    for j in range(0, i + 1):
       print("* ", end="")
    print()


