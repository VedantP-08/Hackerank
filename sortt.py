# Enter your code here. Read input from STDIN. Print output to STDOUT
string = input()
l = []
n = []
odd = []
even =[]
for i in string:
    if i.isalpha():
        l.append(i)
    else:
        n.append(int(i))
l.sort()
for i in range(len(l)):
    for j in range(len(l)):
        if l[i].islower() and l[j].isupper():
            temp = l[i]
            l[i] = l[j]
            l[j] = temp
for i in n:
    if i%2==0:
        even.append(i)
    if i%2!=0:
        odd.append(i)
odd.sort()
even.sort()
sort = ""
for i in l:
    sort+=i
for i in odd:
    i = str(i)
    sort+=i
for i in even:
    i = str(i)
    sort+=i
print(sort)   
    


