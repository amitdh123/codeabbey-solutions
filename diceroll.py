import random
import math

class Diceroll:
	def __init__(self):
		self.randomvalues =  random.randrange(0,1)
		print(self.randomvalues)

	def randomFormat():
		for single_random in self.randomvalues:
			needed_integer = math.floor(single_random)
			return needed_integer


dice = Diceroll()
print(dice.randomFormat());
