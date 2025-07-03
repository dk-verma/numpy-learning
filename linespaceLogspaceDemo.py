from array import array

from numpy import *
print(linspace(0,100,21))

# print(logspace(1,20))

larr = logspace(1,20)

for i in larr:
    print(i)

print(f"arrange(1,25): {arange(1,25)}")
print(f"arange(1,45,5): {arange(1,45,5)}")
print(f"arange(100,1,-2): {arange(100,1,-2)}")
print(f"zeros(12): {zeros(12)}")
print(f"ones(15): {ones(15)}")