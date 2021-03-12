""""
a=input("enter the value of a:")
b=input("enter the value of b:")
c=a+b
print(c)

a=bool(input("enter the value of a:"))
b=float(input("enter the value of b:"))
d=a+b
print(d)

a=10
b=bytes(a)
print(b)

lst=[10,20,3.9,"gaurang"]
print(lst)
lst[1]=100
print (lst)
lst[-1]=100
print (lst)


lst=[10,3.9,True]
print(lst)
lst[4]="hello"
print(lst)

lst=[10,3.9,True]
print(lst)
a="hello"
lst.append(a)
print(lst)

set={10,20.9,10,"hello"}
print(set)
f=frozenset(set)
print(f)
"""

x = range(10, 100, -2)
for n in x:
  print(n)


