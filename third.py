import math
u=int(input("enter the value of u:"))
a=int(input("enter the value of a:"))
s=int(input("enter the value of s:"))
# first eqn of motion
v=(math.sqrt(u**2+2*a*s))
print("the value of first motion of eqn =",v)

#second eqn of motion
t=int(input("enter the value of t:"))
v=u+a*t
print("the value of second motion of eqn=",v)

#third eqn of motion

v=u+(1/2)*a*t**2
print("the value of third motion of eqn=",v)


