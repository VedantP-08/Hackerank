num = int(input())
l1=[]
for i in range(1,num+1):
    if num%i==0:
        l1.append(i)
for j in l1:
    if(j*j == num):
        print(j)