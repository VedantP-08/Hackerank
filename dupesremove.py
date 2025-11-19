nums=[]
n = int(input())
for i in range(n):
    k = int(input())
    nums.append(k)
s1 = set(nums)
total = 0
for j in nums:
    while nums.count(j)!=1:
        nums.remove(j)
print(nums)
print(len(nums))
