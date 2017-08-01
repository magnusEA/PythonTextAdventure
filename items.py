from abc import ABCMeta, abstractmethod

class items:
	__metaclass__ = ABCMeta
	
	@abstractmethod
	def itemName(self): pass
	
	@abstractmethod
	def action(self): pass
	
	@abstractmethod
	def isUsable(self): pass
	
	@abstractmethod
	def isInv(self): pass
	
	@abstractmethod
	def setInInv(self): pass
	
	@abstractmethod
	def amount(self): pass
	
class medicine(items):

	def __init__(self):
		self.inv = False
		self.usable = True
		self.amountCount = 0
	
	def itemName(self):
		return "Medicine"
		
	def action(self):
		return "restores 50 health"
		
	def isUsable(self):
		return self.usable
		
	def isInv(self):
		return self.inv
		
	def setInInv(self):
		self.amountCount += 1
		self.inv = True
		
	def amount(self):
		return self.amountCount

class bandages(items):

	def __init__(self):
		self.inv = False
		self.usable = True
		self.amountCount = 0
		
	def itemName(self):
		return "Bandages"
		
	def action(self):
		return "restores 20 health"
		
	def isUsable(self):
		return self.usable
		
	def isInv(self):
		return self.inv
		
	def setInInv(self):
		self.amountCount += 1
		self.inv = True
		
	def amount(self):
		return self.amountCount
		
class flashlight(items):

	def __init__(self):
		self.inv = False
		self.usable = True
		self.amountCount = 0
		
	def itemName(self):
		return "Flashlight"
		
	def action(self):
		return "lights up a room"
		
	def isUsable(self):
		return self.usable
		
	def isInv(self):
		return self.inv
		
	def setInInv(self):
		self.amountCount += 1
		self.inv = True
		
	def amount(self):
		return self.amountCount
		
class gun(items):

	def __init__(self):
		self.inv = False
		self.usable = True
		self.amountCount = 0
		
	def itemName(self):
		return "Gun"
		
	def action(self):
		return "Deals X amount more damage"
		
	def isUsable(self):
		return self.usable
		
	def isInv(self):
		return self.inv
		
	def setInInv(self):
		# maybe amount count can depend on amount of bullets the player has
		self.amountCount += 1
		self.inv = True
		
	def amount(self):
		return self.amountCount