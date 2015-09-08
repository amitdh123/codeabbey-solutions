class Temperature:
	def __init__(self):
		self.temp1 = 5
		self.temp2 = 13
		self.temp3 = 15
		self.temp4 = 22

	def next(self):
		for temp in [self.temp1 , self.temp2 , self.temp3 , self.temp4]:
			yield temp

	def __iter__(self):
		return self

t = Temperature()
for _t in next(t):
	print(_t)
