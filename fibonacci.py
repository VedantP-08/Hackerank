n = int(input())
l1=[]
def fib(n,l1):
    for i in range(n):
        if i==0 or i==1:
            l1.append(i)
            continue
        if i>1:
            l1.append(fib(i-1)+fib(i-2))
print(l1)