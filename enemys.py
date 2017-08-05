class mutant:
		def __init__(self):
			self.health = 10
		
		def name(self):
			return 'mutant'
			
		def attack(self):
			return 10
			
		def dmgHealth(self, dmg):
			self.health -= dmg 
			
		def getHealth(self):
			return self.health