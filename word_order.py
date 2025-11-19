n  = int(input())
l = list(map(str,input().split()))
vowels = ['a','e','i','o','u']
score = 0
for i in l:
    count = 0
    for j in i:
        if j in vowels:
            count+=1
    if count%2==0:
        score+=2
    else:
        score+=1
print(score)
