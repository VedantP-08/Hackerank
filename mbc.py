import math
side1 = int(input())
side2 = int(input())
side3 = (side1**2 + side2**2)**(1/2)
a = math.asin(side2/side3)
a = a*180/(math.pi)
print(f"{90-round(a)}\N{DEGREE SIGN}")