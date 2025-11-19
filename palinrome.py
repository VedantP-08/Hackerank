class Solution(object):
    def isPalindrome(self, x):
        x = str(x)
        l1=[]
        for i in x:
            l1.append(i)
        k =len(l1)
        total = 0
        for i in range(len(l1)):
            if l1[i]==l1[(k-1)-i]:
                total+=1
        if total==k:
            return True
        else:
            print("false")