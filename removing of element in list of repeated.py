l=[]
n=int(input("enter the size of list:"))
for i in range(n):
	e=int(input(f"enter the element {i} :"))
	l.append(e)
a=int(input("enter the element to be removed:"))	
l.remove(a)
print(l)
