from itertools import groupby
string = input()
s = groupby(string)
for group,count in s:
    print(f"({len(list(count))},{group})",end=" ")
'''d1 = {}
l1=[]
for i in string:
    d1[i] =1
for i in string:
    l1.append(i)
for j in range(len(l1)):'''
    
    

