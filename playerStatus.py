class playerStatus:
	
	def __init__(self):
		self.health = 100
		self.radiation = 0
		
	def displayStatus(self):
		print "Health: ", self.health
		print "Radiation level: ", self.radiation