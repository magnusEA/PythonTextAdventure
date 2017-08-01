from abc import ABCMeta, abstractmethod

class items:
	__metaclass__ = ABCMeta
	
	@abstractmethod
	def itemName(self): pass
	
	@abstractmethod
	def action(self): pass
	
class medicine(items):

	def itemName(self):
		return "Medicine"
		
	def action(self):
		return "restores 50 health"