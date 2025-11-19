from collections import Counter
n = int(input())
l1 =[]
for i in range(n):
    s = input()
    l1.append(s)
l2 = Counter(l1).keys()
l3 = Counter(l1).values()
print(len(l2))
for i in l3:
    print(i, end=" ")
