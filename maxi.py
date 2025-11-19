s = input().split()
k = int(s[0])
m = int(s[1])
l=[]
l1=[]
for i in range(k):
    x = input().split()
    for j in x:
        l1.append(int(j))
    l.append(max(l1))
    l1.clear()
total = 0
for i in l:
    total+=i**2
maxima = total%m
print(maxima)
