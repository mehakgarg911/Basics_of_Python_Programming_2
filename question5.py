class Vehicle:
	def __init__(self,name,mileage,capacity):
		self.name = name
		self.mileage = mileage
		self.capacity = capacity

	def fare(self):
		return self.capacity * 100

class Bus(Vehicle):
	def __init__(self,name,mileage,capacity):
		Vehicle.__init__(self,name,mileage,capacity)

	def fare(self):
		fare = Vehicle.fare(self) + Vehicle.fare(self)*0.1
		return fare


b = Bus("volvo",30,50)
print("Total Bus fare is: ",b.fare())