result_list = []

def vowel_count(items, list1):
	vowel_array = ['a','e','i','o','u','y']
	counter = 0
	for i in range(0, items):
		for j in range(0, len(list1[i])):
			if(list1[j] == vowel_array[j]):
				counter = counter+1			
		result_list.append(counter)
	return result_list

length = 4
list1 = ['abracadabra','pear tree', 'o a kak ushakov lil vo kashu kakao', 'my pyx']
result = vowel_count(length , list1)

print(result)