s = input("enter the string: ")
sub = input("Enter the substring you want to search: ")
l1=[]
l2=[]                   #substring array
for i in s:
    l1.append(i)
for j in sub:
    l2.append(j)
for i in l2:
    x = l1.index(i)
