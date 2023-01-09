#ASSIGNMENT 1
#Q1
p=int(input("first number"))
q=int(input("second number"))
r=int(input("third number"))
s=(p+q+r)/3
print(s)

#Q2
a = float(input("enter your income"))
b = a-10000
c = int(input("dependents"))
d = c*3000
e = b-d
f = (0.2*e)
print(f)

#Q3
from math import *
a = float(input("enter value"))
b = a/60
c = (a%60)
d = "mins"
e = floor(b)
f = "secs"
print(e,str(d),"and",c,str(f))

#Q4
a = int(input("num1"))
b = float(input("num2"))
c = input("num3")
d = a+b+int(c)
print(d)

#Q5
import math
a=0
while a<=345:
    print(math.sin(math.radians(a)), math.cos(math.radians(a)))
    a = a+15

#ASSIGNMENT END