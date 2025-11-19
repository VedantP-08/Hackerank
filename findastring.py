word = input("Enter the word: ")
s = input("Enter the string to be searched: ")
n = len(s)
c = ""
l1=[]
for i in range(len(word)):
    l1.append(word[i:i+n])
for j in l1:
    if len(j)!=n:
        l1.remove(j)
total = 0
for x in l1:
    if x==s:
        total+=1
print(total)



    

    

