x = int(input())
y = str(x)
l1 = []
l2=[]
for i in y:
    l1.append(i)
if x<0:
    l1.remove("-")
k = len(l1)
for j in range(len(l1)):
    l2.append(l1[(k-1)-j])
num = ""
for z in l2:
    num+=z
no = int(num)
if(x>=0):
    print(no)
if(x<0):
    no = 0-no
    print(no)
