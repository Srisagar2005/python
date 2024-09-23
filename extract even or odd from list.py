l=[]
n=int(input("enter the size of list:"))
for i in range(n):
	e=int(input(f"enter the element {i} :"))
	l.append(e)
m=[]
n=[]
for j in l:
    if j%2==0:
        m.append(j)
    else :
        n.append(j)
print(m)
print(n)
