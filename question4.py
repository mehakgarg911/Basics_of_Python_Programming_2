class Vehicle:

	def __init__(self,name,max_speed,mileage):
		self.name = name
		self.max_speed = max_speed
		self.mileage = mileage

	def seating_capacity(self,capacity):
		return f"The seating capacity of a {self.name} is {capacity} passengers."

class Bus(Vehicle):

	def __init__(self,name,max_speed,mileage):
		Vehicle.__init__(self,name,max_speed,mileage)

	def seating_capacity(self,capacity = 50):
		return f"The seating capacity of a {self.name} is {capacity} passengers."


b = Bus("volvo",60,30)
print(b.seating_capacity())