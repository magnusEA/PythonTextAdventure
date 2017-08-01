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
	
class medicine(items):

	def __init__(self):
		self.inv = False
		self.usable = True
	
	def itemName(self):
		return "Medicine"
		
	def action(self):
		return "restores 50 health"
		
	def isUsable(self):
		return self.usable
		
	def isInv(self):
		return self.inv
		
	def setInInv(self):
		self.inv = True
		