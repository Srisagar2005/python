def max_min():
	print(f"the largest element in {l} is {max(l)} and smallest element is {min(l)} ")


l=[]
n=int(input("enter the size of the list:"))
for i in range (n):
	a=int(input('enetr the elements:'))
	l.append(a)
print(l)
max_min()
