s = input()
k = int(input())
l1 = []
l = []
c = 0
str = ""
while c+k<len(s)+1:
    l1.append(s[c:c+k])
    c+=k
for i in l1:
    i = list(dict.fromkeys(i))
    l.append(i)
for i in l:
    for j in i:
        print(j,end="")
    print()





   

