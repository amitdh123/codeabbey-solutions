from decimal import *
class Fahrenheit:
	
	def __init__(self):
		self.temperature1 = 495
		self.temperature2 = 353
		self.temperature3 = 168
		self.temperature4 = -39
		self.temperature5 = 22
		self.celcius_factor = Decimal(5)/ Decimal(9)
	
	def next(self):
		for temp in [self.temperature1 , self.temperature2 , self.temperature3 , self.temperature4 , self.temperature5]:
			temperature = temp -32
			base_fahrenheit = temperature * self.celcius_factor
			final_fahrenheit = round(base_fahrenheit , 2)
			yield final_fahrenheit

	def __iter__(self):
		return self

f = Fahrenheit()
for _f in next(f):
	print(_f)