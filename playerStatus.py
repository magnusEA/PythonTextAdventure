class playerStatus:
	
	def __init__(self):
		self.health = 100
		self.radiation = 0
		
	def displayStatus(self):
		print "Health: ", self.health
		
		# radiation level will be a hidden stat 
		#print "Radiation level: ", self.radiation
		
	#getters
	def getHealth(self):
		return self.health
		
	def getRadiation(self):
		return self.radiation
		
	#setters
	def setHealth(self, hp):
		self.health = hp
		
	def setRadiation(self, rad):
		self.radiation = rad
	
	def attack(self):
		return 10
		
	def dmgHealth(self, dmg):
		self.health -= dmg