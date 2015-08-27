def sumloop(items, numberlist ):
	sum = 0;
	for i in range(0,items):
		sum = sum + numberlist[i]
	return sum

length = 5
numberlist = [1,5,0,4,3,]
result = sumloop(length,numberlist)
print(result)