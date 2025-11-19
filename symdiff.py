l1 = []
l2 = []
m  = int(input())
sm = input().split()
for i in sm:
    if len(l1)<=len(sm):
        l1.append(int(i)) 
n = int(input())
sn = input().split()
for i in sn:
    if len(l2)<=len(sn):
        l2.append(int(i))
l = []
for i in l1:
    if i not in l2:
        l.append(i)
for j in l2:
    if j not in l1:
        l.append(j)
l.sort()
l = list(dict.fromkeys(l))
for k in l:
    print(k)