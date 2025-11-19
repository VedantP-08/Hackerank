from collections import defaultdict
s = input().split()
n = int(s[0])
m = int(s[1])
lA = []
lB = []
l1=[]
d = defaultdict(list)
for i in range(n):
    i = input()
    lA.append(i)
for i in lA:
    l1.append(i)
for i in range (m):
    i = input()
    lB.append(i)
for i in lB:
    while i in lA:
        k = lA.index(i)
        d[i].append(k+1)
        lA[k] = " "
for i in lB:
    if i not in l1:
        d[i].append(-1)
for i in d.values():
    for j in i:
        print(j, end=" ")
    print()



        
