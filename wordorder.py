n = int(input())
l1 = []
d1 = {}
for i in range(n):
    s = input()
    l1.append(s)
for i in range(len(l1)):
    d1[l1[i]] = l1.count(l1[i]) 
print(len(d1))
for i in d1.values():
    print(i,end=" ")

    


    