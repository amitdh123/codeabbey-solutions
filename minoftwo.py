resultlist = []

def minOfTwo(items, list1 , list2):
	for i in range(0,items):
		min = list1[i]
		if(list2[i] < min):
			min = list2[i]
		resultlist.append(min)
	return resultlist

length = 3
list1 = [5,2,100]
list2 = [3,8,15]
result = minOfTwo(length, list1 , list2)
print(result)
