n = input().split()
rows = int(n[1])
columns = int(n[0])
l1=[]
marks=[]
for i in range(rows):
    mark = list(map(float,input().split()))
    marks.append(mark)
stud = list(zip(*marks))
final = []
for i in stud:
    final.append(sum(i))
for j in final:
    print(f"{j:.1f}")