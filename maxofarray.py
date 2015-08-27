resultlist = []
def maxMinOfArray(items):
	max = items[0]
	min = items[0]
	for i in range(0, len(items)):
		if(items[i] > max):
			max = items[i]
		if(items[i] < min):
			min = items[i]
	resultlist.append(max)
	resultlist.append(min)
	return resultlist

array = [5,6,6,1,8,34,98,54,23,7,1,4,110,267,42,142,78,98,5,7]
result = maxMinOfArray(array)
print(result)