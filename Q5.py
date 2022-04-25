#Q5
from math import pi,sin,cos
deg=0
y=0
z=0
for deg in range(0,346,15):
 rad= deg*(pi/180)
 y=round(sin(rad),4)
 z=round(cos(rad),4)
print("sin",deg,"=",y,"and cos",deg,"=",z
