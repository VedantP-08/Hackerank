 n = len(string)
    l1 = []
    l = []
    vowels = ['A','E','I','O','U']
    v = []
    c = []
    for i in range(n+1):
        for j in range(n):
            l1.append(string[j:j+i])
    while '' in l1:
        l1.remove('')
    l = list(dict.fromkeys(l1))
    for i in l:
        if i[0] not in vowels:
            c.append(i)
        else:
            v.append(i)
    stuart = 0
    kevin = 1
    for i in c:
        stuart+=string.count(i)
    for i in v:
        kevin+=string.count(i)
    if(stuart>kevin):
        print(f"Stuart {stuart}")
    else:
        print(f"Kevin {kevin}")