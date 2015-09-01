import math

result_list = []

def rounding(items, list1 , list2):
	for i in range(0,items):
		divided_number = 1.0 * list1[i]/list2[i]		
		if(divided_number == float(divided_number)):
			unrounded_number = round(divided_number , 2)
			if(unrounded_number < 0):
				new_unrounded_number = unrounded_number - int(unrounded_number)	
				result_initial = 1 + new_unrounded_number
				final_result = unrounded_number - result_initial
			else:
				new_unrounded_number = unrounded_number - int(unrounded_number)
				result_initial = 1 - new_unrounded_number
				print(result_initial)
				final_result = unrounded_number + result_initial
		else:
			new_unrounded_number = divided_number

		
		

		result_list.append(final_result)

	return result_list

length = 3
list1 = [12,11,400]
list2 = [8,-3,5]
result = rounding(length , list1 , list2)
print(result)

