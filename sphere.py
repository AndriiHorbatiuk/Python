import math
class Sphere:
	def __init__(self,radius=1,x=0.0,y=0.0,z=0.0):
		self.radius = radius
		self.x = x
		self.y = y
		self.z = z

	def get_volume(self):
		self.v = math.pi * pow(self.radius,3) * 4 / 3
		return self.v

	def get_square(self):
		self.square = 4 * math.pi * pow(self.radius,2)
		return self.square

	def get_radius(self):
		return self.radius

	def get_center(self):
		self.center = (self.x, self.y, self.z)
		return self.center

	def set_radius(self,r):
		self.radius = r

	def set_center(self,x,y,z):
		self.x = x
		self.y = y
		self.z = z

	def is_point_inside(self,x,y,z):
		self.x1 = x
		self.y2 = y
		self.z2 = z
		
		if pow((self.x - self.x1),2) + pow((self.y - self.y2),2) + pow((self.z - self.z2),2) < pow(self.radius,2):
			return True
		else:
			return False

s0 = Sphere(0.5)
print s0.get_volume()
print s0.get_square()
print s0.get_center()
s0.set_radius(1.6) 
print s0.is_point_inside(0, -1.5, 0)
print s0.get_radius()
