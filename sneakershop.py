n = int(input())
s = input().split()
l1=[]
sizes=[]
prices=[]
for i in s:
    l1.append(int(i))
n2 = int(input())
for i in range(n2):
    order = input().split()
    sizes.append(int(order[0]))
    prices.append(int(order[1]))
total = 0
for i in sizes:
    if i in l1:
        k = sizes.index(i)
        total+=prices[k]
        prices.pop(k)
        sizes.pop(k)
        x = l1.index(i)
        l1.pop(x)
print(total)

    








    
