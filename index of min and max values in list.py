l=[]
n=int(input("enter the size of list:"))
for i in range(n):
	e=int(input(f"enter the element {i} :"))
	l.append(e)
print("the minimum value of ",l,"has index:",l.index(min(l)))
print("the maximum value of ",l,"has index:",l.index(max(l)))
