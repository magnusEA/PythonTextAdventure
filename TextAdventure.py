# coding: utf-8

# import files
import items
import playerStatus

# initalize classes
m = items.medicine()
PS = playerStatus.playerStatus()

displayMessage = True

# append classes (will use a list to contain all classes within a list) 
it = []
it.append(m)

def RunChoice(pickChoice):
	displayChoice = choices[pickChoice]
	print displayChoice[0:len(displayChoice) - 4]
	
	# get input from user
	pick = raw_input("> ")
	
	# check if input is a number (helps with avoiding inputs other than numbers) 
	try:
		int(pick) # if number then do except
	except ValueError:
		print "Type only numbers"
		RunChoice(pickChoice)
		return # end this function to avoid issues 
	
	# search for user input to know what they choose & display that
	pick2 = int(pick)+1
	userGot = displayChoice[displayChoice.find(pick)+3:displayChoice.find(str(pick2))-2]

	# check if string isn't null 
	if userGot:
		letter = displayChoice[-1:]
		print choiceAction[letter], userGot
		
		# use list of classes to determine if item/thing is done or used to be used later when determining what branchs
		# to take later on in the story 
		for item in it:
			if (item.itemName() == userGot):
				print "GOT IT"
				break
	else:
		#if not found try again 
		print "Try again"
		RunChoice(pickChoice)
		return 
		
def DisplayStory(display):
	#foreach index print story
	for s in display:
		#get first char from list like so s[0]
		if(s[0] == '('):
			#print everything after )
			print s[s.find(')')+1:]
			
			#display choices 
			RunChoice(s[s.find('(') + 1:s.find(')')])

			#wait for user input to conitune 
			userInput()
		else:
			#else print normally
			print s
			
			#wait for user input to conitune 
			userInput()
	
	# At end of function find next branch to be displayed 
	# I'd imagine here we'd have a lot of condition statements
	# checking for whos alive, items held, etc to determine which branch or list
	# to run next 
	print "END OF DISPLAY"

def commandList():
	print "status: Display information of your player's health"

def userInput():
	global displayMessage
	if(displayMessage == True):
		print "Press Enter to conitune or type Help for list of commands:"
		displayMessage = False
		
	get = raw_input("> ")
	
	if(get == 'help' or get == 'Help'):
		commandList()
		userInput()
		return
	elif(get == 'status' or get == 'Status'):
		#display player status
		PS.displayStatus()
		userInput()
		return
		
	#otherwise do nothing 
	
# append all choice actions in dict
choiceAction = {
'A': 'You decide to take'
}
		
# append all choices in dict
choices = {
'Ch1Choice1': 'I can take: 1. Medicine, 2. Bandages, 3. Flashlight, 4. Gun, 5.A'
}
		
# append all story (list for each branch of story)
# get player name first before appending 
playerName = raw_input("Enter player name:" )
story = []
chapter1 = []
chapter1.append('''You wake up to a very loud alarm 
You are surrounded by dark musty walls. Almost like in a prison cell. 
But this is just how it is everyday underground. 
This is just one of the daily reminders of how humanity has fallen and the horrors you have to face just to survive.
''') 
chapter1.append('''(Ch1Choice1)You get yourself together and begin to gather your supplies because today is a special day the day you get to venture out in the surface with the rest of...them.
You pack some food, water, pickaxe, shovel, rope, and a knife. 
Just before heading out your door frame where a door would be normally placed you decide to bring with you one last thing. 
''')
chapter1.append('''As you step outside your door frame you look up to see the ceiling just dirt and rocks.''')
chapter1.append('''You feel a little excited as well as terrified knowing by this time tomorrow you’ll be outside on the surface being able to look at the sky.''')
chapter1.append('''You begin making your way to just outside the exit of this underground city.''')
chapter1.append('''There the expedition leader will be waiting as well as everyone else going to the surface.''')
chapter1.append('''You arrive at the meeting point, you quite a few people here at least for a run to the outside. Including your long time friend Bob, who comes over to you to greet you.''')
chapter1.append('''Bob: “Hey, ''' + playerName + ''' I hope you got everything packed. Seems quite a few more people are going this time around than previous times. I guess it’s because this will be the first time humanity is going all the way to the surface rather than just digging holes that might reach the surface.” ''')
chapter1.append(playerName + ''': “Yeah seems like it. I think everything should go smoothly. The last diggers  said that they’ve finally made a path all the way to the sewers of the surface.Though they stopped in fear of the radiation up there."''')
chapter1.append('''Bob: “True, but today is different. Today they said they’ll have radiation suits to help protect us from the radiation. Though I wonder where they even found the suits.”''')
chapter1.append('''Just before you could speak the main expedition leader, Joule, stepped up in front and began to speak. He has lead many expeditions time and time again. Every expedition was spent digging to clear the rubble blocking the path to the surface caused by the bombs that destroyed our previous world.''')
chapter1.append('''Joule: “Today we can finally begin our journey to reclaim the surface that is rightfully ours.”''')
chapter1.append('''Joule: “Because of the limited supply of radiation suits we were able to acquire from the last expedition only 8 of us will be able to go. I’ve narrowed it down the 8 strongest and bravest people we have based on all previous expeditions.”''')


DisplayStory(chapter1)
