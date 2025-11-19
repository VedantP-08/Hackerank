from itertools import permutations
n = int(input())
l = list(map(str,input().split()))
k = int(input())
index = []
for i in l:
    if i =="a":
        index.append(l.index(i))
combo = list(permutations(index,k))
for i in index:
    for j in combo:
        if i in j:
            total+=1
prob = float(total/len(combo))
print(f"{prob:.3f}")
        