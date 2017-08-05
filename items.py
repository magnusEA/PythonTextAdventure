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

class takeLantern(items):

	def __init__(self):
		self.inv = False
		self.usable = False
		self.branch = True
		
	def itemName(self):
		return "Take lantern"
		
	def displayText(self):
		return "To take the lantern"
		
	def action(self):
		return self.branch
		
	def isUsable(self):
		return self.usable
		
	def isInv(self):
		return self.inv
		
	def setInInv(self):
		# make usable to be checked later 
		self.usable = True		
		
	def amount(self):
		return self.amountCount	
		
	def getBranch(self):
		return 'chapter2TakeLantern'

	def setBranchToFalse(self):
		self.branch = False
		
class dontLantern(items):

	def __init__(self):
		self.inv = False
		self.usable = False
		self.branch = True
		
	def itemName(self):
		return "Leave lantern"
		
	def displayText(self):
		return "To leave the lantern"
		
	def action(self):
		return self.branch
		
	def isUsable(self):
		return self.usable
		
	def isInv(self):
		return self.inv
		
	def setInInv(self):
		# make usable to be checked later 
		self.usable = True		
		
	def amount(self):
		return self.amountCount	
		
	def getBranch(self):
		return 'chapter2DontTakeLantern'

	def setBranchToFalse(self):
		self.branch = False
		
# non-items------------------------------------------------------------------------------------------------		
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
		
class findJim(items):

	def __init__(self):
		self.inv = False
		self.usable = False
		self.branch = True
		
	def itemName(self):
		return "Wake up Bob to help find Jim"
		
	def displayText(self):
		return "You wake up Jim."
		
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
		return 'chapter2BranchA'

	def setBranchToFalse(self):
		self.branch = False
		
class findJimAlone(items):

	def __init__(self):
		self.inv = False
		self.usable = False
		self.branch = True
		
	def itemName(self):
		return "Look for Jim alone"
		
	def displayText(self):
		return "to not wake anyone up"
		
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
		return 'chapter2BranchB'

	def setBranchToFalse(self):
		self.branch = False
		
class wakeEveryone(items):

	def __init__(self):
		self.inv = False
		self.usable = False
		self.branch = True
		
	def itemName(self):
		return "Wake everyone up to help find Jim"
		
	def displayText(self):
		return "wake everyone up"
		
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
		return 'chapter2BranchC'

	def setBranchToFalse(self):
		self.branch = False
		
class hillUseExp(items):

	def __init__(self):
		self.inv = False
		self.usable = False
		self.branch = True
		
	def itemName(self):
		return "Let Hill use explosives"
		
	def displayText(self):
		return "To let Hill use the explosives"
		
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
		return 'chapter3UseHillExp'

	def setBranchToFalse(self):
		self.branch = False
	
	
class hillDonExp(items):

	def __init__(self):
		self.inv = False
		self.usable = False
		self.branch = True
		
	def itemName(self):
		return "Don\'t let Hill use his explosives"
		
	def displayText(self):
		return "Not to let Hill use explosives"
		
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
		return 'chapter3DonUseExp'

	def setBranchToFalse(self):
		self.branch = False