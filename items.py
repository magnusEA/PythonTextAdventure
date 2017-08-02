from abc import ABCMeta, abstractmethod

class items:
	__metaclass__ = ABCMeta
	
	@abstractmethod
	def itemName(self): pass
	
	@abstractmethod
	def displayText(self): pass
	
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
		self.usable = False
		self.amountCount = 0
	
	def itemName(self):
		return "Medicine"
		
	def displayText(self):
		return "This will prevent any infections in case I get a cut."
	
	def action(self):
		return "restores 50 health"
		
	def isUsable(self):
		return self.usable
		
	def isInv(self):
		return self.inv
		
	def setInInv(self):
		self.usable = True
		self.inv = True
		
	def amount(self):
		return self.amountCount

class bandages(items):

	def __init__(self):
		self.inv = False
		self.usable = False
		self.amountCount = 0
		
	def itemName(self):
		return "Bandages"
		
	def displayText(self):
		return "In case of any acidents I'll take some bandages."
		
	def action(self):
		return "restores 20 health"
		
	def isUsable(self):
		return self.usable
		
	def isInv(self):
		return self.inv
		
	def setInInv(self):
		self.usable = True
		self.inv = True
		
	def amount(self):
		return self.amountCount
		
class flashlight(items):

	def __init__(self):
		self.inv = False
		self.usable = False
		self.amountCount = 0
		
	def itemName(self):
		return "Flashlight"
	
	def displayText(self):
		return "Always helpful to take a spare."
		
	def action(self):
		return "lights up a room"
		
	def isUsable(self):
		return self.usable
		
	def isInv(self):
		return self.inv
		
	def setInInv(self):
		self.usable = True
		self.inv = True
		
	def amount(self):
		return self.amountCount
		
class gun(items):

	def __init__(self):
		self.inv = False
		self.usable = False
		self.amountCount = 0
		
	def itemName(self):
		return "Gun"
		
	def displayText(self):
		return "the Gun. Looks like it only has 2 shots"
		
	def action(self):
		return "Deals X amount more damage"
		
	def isUsable(self):
		return self.usable
		
	def isInv(self):
		return self.inv
		
	def setInInv(self):
		self.amountCount = 2
		self.usable = True
		self.inv = True
		
	def amount(self):
		return self.amountCount
		
class jimSaid(items):
	
	def __init__(self):
		self.inv = False
		self.usable = False
		self.branch = True
		
	def itemName(self):
		return "Let him know what Jim said"
		
	def displayText(self):
		return "Jim said..."
		
	def action(self):
		return self.branch
		
	def isUsable(self):
		return self.usable
		
	def isInv(self):
		return self.inv
		
	def setInInv(self):
		# make usable to be checked later 
		self.usable = True
		# don't set in inventory 
		self.inv = False
		
	def amount(self):
		return self.amountCount
		
	def getBranch(self):
		return 'chapter1branchA'

	def setBranchToFalse(self):
		self.branch = False
		
class dontBob(items):
	
	def __init__(self):
		self.inv = False
		self.usable = False
		self.branch = True
		
	def itemName(self):
		return "Don\'t tell Bob anything"
		
	def displayText(self):
		return "It's nothing important."
		
	def action(self):
		return self.branch
		
	def isUsable(self):
		return self.usable
		
	def isInv(self):
		return self.inv
		
	def setInInv(self):
		# make usable to be checked later 
		self.usable = True
		# don't set in inventory 
		self.inv = False
		
	def amount(self):
		return self.amountCount
		
	def getBranch(self):
		return 'chapter1branchB'

	def setBranchToFalse(self):
		self.branch = False
		
class changeTopic(items):

	def __init__(self):
		self.inv = False
		self.usable = False
		self.branch = True
		
	def itemName(self):
		return "Change the topic"
		
	def displayText(self):
		return "We shouldn\'t keep Joule waiting."
		
	def action(self):
		return self.branch
		
	def isUsable(self):
		return self.usable
		
	def isInv(self):
		return self.inv
		
	def setInInv(self):
		# make usable to be checked later 
		self.usable = True
		# don't set in inventory 
		self.inv = False
		
	def amount(self):
		return self.amountCount
		
	def getBranch(self):
		return 'chapter1branchC'

	def setBranchToFalse(self):
		self.branch = False