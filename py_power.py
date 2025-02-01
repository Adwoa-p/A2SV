from math import pow
a = int(input())
b = int(input())
m = int(input())

x = pow(a,b)
print(int(x))

if b > 0:
    y = (a**b)%m
    print(y)
