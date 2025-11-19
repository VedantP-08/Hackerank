from itertools import combinations
str = input().split()
s = str[0]
k = int(str[1])
l=[]
final=[]
for i in range(1,k+1):
    l=list(combinations(s,i))
    l.sort()
    for i in l:
        i=list(i)
        i.sort()
        final.append(i)
    l.clear()
l2=[]
for i in final:
    i.sort()
    for j in i:
        n+=j
        l2.append(n)
    n=""
l2.sort()
for i in l2:
    print(i)


