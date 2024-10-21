def max_min(l):
	l=list(set(l))
	l.sort()
	print("the second largest element in the list :",l," is :",l[-2])


l=[]
n=int(input("enter the size of the list:"))
for i in range (1,n+1):
	a=int(input(f'enetr the element{i}:'))
	l.append(a)
	
max_min(l)
