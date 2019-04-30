class Human:
	count = 0	
	def __init__(self, name):
		self.name = name
		Human.count += 1
		self.id = Human.count

A = Human('drx')
print A.id
print Human.count
B = Human('doublevkay')
print B.id
print Human.count

