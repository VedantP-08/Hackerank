s = input()
l1 = []
l2 = []
for i in s:
    l1.append(i)
for j in range(len(l1)):
    if j ==0:
        x = l1[0]
        y = x.upper()
        l1[0] = y
    if l1[j]==" ":
        k = l1[j+1]
        c = k.upper()
        l1[j+1] =c
str = ""
for i in l1:
    str+=i
print(str)









    
