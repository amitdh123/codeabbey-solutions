resultlist = []

def minOfTwo(items, list1 , list2 , list3):
	for i in range(0,items):
		min = list1[i]
		if(list2[i] < min):
			min = list2[i]
		if(list3[i] < min):
			min = list3[i]
		resultlist.append(min)
	return resultlist

length = 3
list1 = [7,15,300]
list2 = [3,20,550]
list3 = [5,4,137]
result = minOfTwo(length, list1 , list2 , list3)
print(result)
