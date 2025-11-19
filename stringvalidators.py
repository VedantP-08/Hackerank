s = input()
alnum = 0
alpha = 0
dig = 0
lower = 0
upper = 0
for i in s:
    if(i.isalnum()==True):
        alnum +=1
    if(i.isalpha() == True):
        alpha+=1
    if(i.isdigit()==True):
        dig+=1
    if(i.isupper()==True):
        upper+=1
    if(i.islower() == True):
        lower+=1
if(alnum > 0):
    print(True)
if(alnum == 0):
    print(False)
if(alpha>0):
    print(True)
if(alpha==0):
    print(False)
if(dig>0):
    print(True)
if(dig==0):
    print(False)
if(upper>0):
    print(True)
if(upper==0):
    print(False)
if(lower>0):
    print(True)
if(lower==0):
    print(False)

    

    
