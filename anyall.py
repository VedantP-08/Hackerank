n = int(input())
l1 = list(map(int,input().split()))
rev = 0
reverse = []
for i in l1:
    while i>0:
        r = i%10
        i = int(i/10)
        rev = rev*10+r
        reverse.append(rev)
total = 0
pal = 0
for i in range(n):
    if l1[i]>0:
        total+=1
    if l1[i]==reverse[i]:
        pal+=1
    print(all(total ==n,pal>0))
    
            
