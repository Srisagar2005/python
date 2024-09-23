l=[]
n=int(input("enter the size of list:"))
for i in range(n):
	e=int(input(f"enter the element {i} :"))
	l.append(e)
l[0],l[-1]=l[-1],l[0]
print(f"after reversing the frist and last elements: {l}")
