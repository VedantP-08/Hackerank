n = int(input())
nums=[]
l1=[]
for i in range(n):
    i = int(input())
    nums.append(i)
target = int(input())
for i in range(len(nums)):
    for j in range(1,i):
        if nums[i]+nums[i+j]==target:
            while len(l1)<2:
                l1.append(i)
                l1.append(j)
       
print(l1)

    

