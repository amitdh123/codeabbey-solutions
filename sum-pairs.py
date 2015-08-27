resultlist = []
def sumpairs(items, pair1 , pair2):
	sum = 0
	for i in range(0,items):
		sum = pair1[i]+pair2[i]
		resultlist.append(sum);
	return resultlist

length = 3
pair1 = [100, 15,1945]
pair2 = [8,245,54]
result = sumpairs(length, pair1 , pair2)
print(result)

