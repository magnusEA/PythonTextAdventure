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
#'Ch1Choice2': 'What do I tell Bob?: 1. Let him know what Jim said, 2. Don\'t tell Bob anything, 3. Change the topic'
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
chapter1.append('''You feel a little excited as well as terrified knowing by this time tomorrow you\
’ll be outside on the surface being able to look at the sky.''')
chapter1.append('''You begin making your way to just outside the exit of this underground city.''')
chapter1.append('''There the expedition leader will be waiting as well as everyone else going to the surface.''')
chapter1.append('''You arrive at the meeting point, you quite a few people here at least for a run to the outside. Including your long time friend Bob, who comes over to you to greet you.''')
chapter1.append('''Bob: “Hey, ''' + playerName + ''' I hope you got everything packed. Seems quite a few more people are going this time around than previous times. I guess it’s because this will be the first time humanity is going all the way to the surface rather than just digging holes that might reach the surface.” ''')
chapter1.append(playerName + ''': “Yeah seems like it. I think everything should go smoothly. The last diggers said that they\’ve finally made a path all the way to the sewers of the surface.Though they stopped in fear of the radiation up there."''')
chapter1.append('''Bob: “True, but today is different. Today they said they’ll have radiation suits to help protect us from the radiation. Though I wonder where they even found the suits.”''')
chapter1.append('''Just before you could speak the main expedition leader, Joule, stepped up in front and began to speak. He has lead many expeditions time and time again. Every expedition was spent digging to clear the rubble blocking the path to the surface caused by the bombs that destroyed our previous world.''')
chapter1.append('''Joule: “Today we can finally begin our journey to reclaim the surface that is rightfully ours.”''')
chapter1.append('''Joule: “Because of the limited supply of radiation suits we were able to acquire from the last expedition only 8 of us will be able to go. I’ve narrowed it down the 8 strongest and bravest people we have based on all previous expeditions.”''')
chapter1.append(playerName + ''': I've met or heard of most of these guys.''')
chapter1.append('''First there is Hill. He is an expert when it comes to making bombs and blowing up holes to make new pathways.''')
chapter1.append('''Next is Jim. He the strongest one out of all of us. He is the go to guy when it comes to getting any physical labor done.''')
chapter1.append('''Yuma is next up. He is all around good at most things, but what sets him apart is his jokes. He is great at keeping moral high.''')
chapter1.append('''Tanner seems like an odd choice. He has a gun and is the best shot so I guess it would make sense to bring him along. Just in case.''')
chapter1.append('''Cody isn't much about physical labor, but he is incredibly smart. He is the one who documents expeditions and gives us advice on how to proceed.''')
chapter1.append('''Bob is the one I trust the most. We have been through a lot. We were both chosen to go because of how many mistakes we fix and prevent.''')
chapter1.append('''Joule is the one leading this expedition. He has been through this the most and can easily guide us through the tunnels.''')
chapter1.append('''Joule: “Now one last thing before we start heading out recently there have been some odd signals coming on our seismograph. We assume they must be small earthquakes but it’s odd because they’ve been going on for quite a while. It doesn’t seem like just one but it’s been multiple for a few days now.”''')
chapter1.append('''Everyone looks at each other with worry in their eyes. ''')
chapter1.append('''Joule: “But do not worry. It has stopped for a few days now and there are no signs that point to more. Hopefully we should be fine since these readings are coming further in our cave system.” ''')
chapter1.append('''Joule: "The earthquakes may have caused some rocks to block our path forwards, but it’s nothing we can’t manage. If the rubble is too much we will have to reschedule this expedition. That however is an absolute last resort. ''')
chapter1.append('''Joule: “Everyone suit up and get ready! We head out in 10 minutes!” ''')
chapter1.append('''Jim: "Hey,'''+playerName+'''..."''')
chapter1.append('''I\'ve only met Jim once and that was on an expedition not to long ago. We went south when a cave in occurred blocking my way back. Luckily, Jim was there and was able to make his way over to me. The speed of his digging got me out before I even realized that I was trapped ''')
chapter1.append('''Bob: "What do you think he wants ''' +playerName+'''?''')
chapter1.append('''I looked over to Bob and shook my head ''')
chapter1.append(playerName +''': “I don’t know. I’ll go see what he wants”  ''')
chapter1.append('''I walk over to Jim ''')
chapter1.append(playerName+ ''': "Hey Jim, something you want to tell me? ''')
chapter1.append('''Jim gave me a hard look in the eyes and whispered to me ''')
chapter1.append('''Jim: “Don\’t trust Joule…” ''')
chapter1.append(playerName+''': “Why not?” ''')
chapter1.append('''Jim: “Every time I’ve been with him on an expedition someone always goes missing. Every time the group wants to go find that missing person Joule refuses. He says something like “The sacrifice of one is needed to help the many.” Needless to say Joule refuses to spend anytime looking for a missing person.” ''')
chapter1.append(playerName+''': “Why are you telling me this? Shouldn’t this be something that everyone should know?” ''')
chapter1.append('''Jim: "I don\'t trust everyone here. He has allies who are on his side. I can\'t prove who, but if Joule is getting away with this time and time again then he clearly must have people on his side helping him. This happens far too much to just be a coincidence. ''')
chapter1.append('''Jim: “Just be sure to stay on your guard. I’m telling you this because I feel like I can trust you.” ''')
chapter1.append(playerName + ''': “Well thank you for telling me. I will keep an eye out and if I notice anything I’ll share the information with you.” ''')
chapter1.append('''Jim: “I\'ll do the same. Let’s watch each other's backs.”''')
chapter1.append('''I walked back over to Bob ''')
chapter1.append('''Bob: “What happened? Is everything alright between you two?” ''')
chapter1.append('''(Ch1Choice2) ''')


DisplayStory(chapter1)