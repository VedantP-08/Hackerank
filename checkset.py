t = int(input())
for i in range(t):
    a= int(input())
    lA = list(map(int,input().split()))
    b = int(input())
    lb = list(map(int,input().split()))
    total = 0
    for j in lA:
        if j in lb:
            total+=1
    if total == a:
        print(True)
    else:
        print(False)
    total = 0



