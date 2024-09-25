l=[]
n=int(input("enter the size of list:"))
for i in range(n):
	e=int(input(f"enter the element {i} :"))
	l.append(e)
print(f"sum of the elements {l} are :",sum(l))
print(f"sum of the elements {l} are :",sum(l)/len(l))	
