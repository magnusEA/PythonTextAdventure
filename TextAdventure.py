# coding: utf-8

# import files
import items
import playerStatus
import enemys
displayMessage = True

# append classes (will use a list to contain all classes within a list) 
it = []
en = []
PS = playerStatus.playerStatus()
it.append(items.medicine())
it.append(items.bandages())
it.append(items.flashlight())
it.append(items.gun())
it.append(items.jimSaid())
it.append(items.dontBob())
it.append(items.changeTopic())
it.append(items.findJim())
it.append(items.findJimAlone())
it.append(items.wakeEveryone())
it.append(items.takeLantern())
it.append(items.dontLantern())
it.append(items.hillUseExp())
it.append(items.hillDonExp())

en.append(enemys.mutant())

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
		#print choiceAction[letter], userGot
		
		# use list of classes to determine if item/thing is done or used to be used later when determining what branchs
		# to take later on in the story 
		for x in range(0, len(it)):
			if (it[x].itemName() == userGot):
				print choiceAction[letter], it[x].displayText()
				it[x].setInInv()
				break
	else:
		#if not found try again 
		print "Try again"
		RunChoice(pickChoice)
		return 

def checkHealth(health):
	if(health <= 0):
		print "You died!"
		return True

def checkEnemyHealth(health):
	if(health <= 0):
		print "It\'s dead!"
		return True
		
def enemyAttack(eninx):
	death = False
	PS.dmgHealth(en[eninx].attack())
	print en[eninx].name() + " dealt " + str(en[eninx].attack()) + " damage to you!"
	
	# check player health
	death = checkHealth(PS.health)
	
	if(death == True):
		print "GAME OVER"
		return
	
	print "Your turn"
	battle(eninx)
		
def battle(eninx):
	dead = False
	get = raw_input("> ")
	if(get == 'attack' or get == 'Attack'):
		en[eninx].dmgHealth(PS.attack())
		print "you dealt " + str(PS.attack()) + " to " + str(en[eninx].name())
		dead = checkEnemyHealth(en[eninx].getHealth())
		
		if(dead == True):
			# exit function 
			return
			
		# enemy turn to attack 
		raw_input("> ")
		enemyAttack(eninx)
	else:
		battle(eninx)
		
def battleWho(battleThis):
	eindx = 0
	for x in range(0, len(en)):
		if(en[x].name() == battleThis):
			eindx = x
			print "FOUND"
			break
	print "Fighting " + battleThis
	battle(eindx)
		
def DisplayStory(display):
	#foreach index print story
	for s in display:
		#if battle do this 
		if(s[0] == '(' and s[1] == 'B'):
			e = s[s.find(':')+1:s.find(')')]
			battleWho(e)
		#get first char from list like so s[0]
		elif(s[0] == '('):
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
	# check if any branch to display in story 
	nextBranch()

# will handle calling next branch of story
def nextBranch():
		#set boolean values to false to start 

		for x in range(0, len(it)):
			# if single condition branch do this 
			if(it[x].isUsable() == True and it[x].action() == True):
				brh = it[x].getBranch()
				# set branch to false to avoid calling it again 
				it[x].setBranchToFalse()
				
				# call displayStory with new branch 
				if(brh == 'chapter1branchA'):
					DisplayStory(chapter1BranchA)
				elif(brh == 'chapter1branchB'):
					DisplayStory(chapter1BranchB)
				elif(brh == 'chapter1branchC'):
					DisplayStory(chapter1BranchC)
				elif(brh == 'chapter2BranchA'):
					DisplayStory(chapter2BranchA)
				elif(brh == 'chapter2BranchB'):
					DisplayStory(chapter2BranchB)
				elif(brh == 'chapter2BranchC'):
					DisplayStory(chapter2BranchC)	
				elif(brh == 'chapter2TakeLantern'):
					DisplayStory(chapter2TakeLantern)
				elif(brh == 'chapter2DontTakeLantern'):
					DisplayStory(chapter2DontTakeLantern)
				elif(brh == 'chapter3HillAlivePart1'):
					DisplayStory(chapter3HillAlivePart1)
				elif(brh == 'chapter3DonUseExp'):
					DisplayStory(chapter3DonUseExp)
				elif(brh == 'chapter3UseHillExp'):
					DisplayStory(chapter3UseHillExp)
		
			# otherwise handle multiple condition branchs
	
def commandList():
	print "status: Display information of your player's health"
	print "inv: Will display your inventory"
	print "use item: Will use item given the name"

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
	elif(get == 'inv' or get == 'Inv'):
		
		#display player inventory
		for i in it:
			if(i.isInv() == True):
				print i.itemName()
		userInput()
		return
		
	#otherwise do nothing 

def branchThis():
	bobAlive = False
	tannerAlive = False
	hillAlive = False
	yumaAlive = False
	codyAlive = False
	
	for x in it:
		if(x.itemName() == 'Wake up Bob to help find Jim' and x.isUsable()):
			bobAlive = True
			
		elif(x.itemName() == 'Take lantern' and x.isUsable()):
			tannerAlive = True
			
		elif(x.itemName() == 'Leave lantern' and x.isUsable()):
			hillAlive = True
			codyAlive = True
			tannerAlive = True
			
		elif(x.itemName() == 'Wake everyone up to help find Jim' and x.isUsable()):
			bobAlive = True
			
	# if all dead do this 
	if(bobAlive and tannerAlive == False and hillAlive == False and yumaAlive == False and codyAlive == False):
		DisplayStory(chapter3BobAlivePart1)
		DisplayStory(chapter3BobAlivePart2)
		DisplayStory(chapter3BobAlivePart3)
		
	elif(bobAlive and tannerAlive and hillAlive == False and codyAlive == False and yumaAlive == False):
		DisplayStory(chapter3BobAlivePart1)
		DisplayStory(chapter3BobAlivePart2)
		DisplayStory(chapter3TannerAlivePart1)
		DisplayStory(chapter3BobAlivePart3)
	elif(bobAlive and tannerAlive and hillAlive == True and codyAlive == True and yumaAlive == False):
		DisplayStory(chapter3BobAlivePart1)
		DisplayStory(chapter3CodyAlivePart1)
		DisplayStory(chapter3BobAlivePart2)
		DisplayStory(chapter3TannerAlivePart1)
		DisplayStory(chapter3BobAlivePart3)
		DisplayStory(chpater3HillAlivePart1)
	
# append all choice actions in dict
choiceAction = {
'A': 'You decide to take',
'B': 'You tell Bob:', 
'C': 'You decide to:'
}
		
# append all choices in dict
choices = {
'Ch1Choice1': 'I can take: 1. Medicine, 2. Bandages, 3. Flashlight, 4. Gun, 5.A',
'Ch1Choice2': 'What do I tell Bob?: 1. Let him know what Jim said, 2. Don\'t tell Bob anything, 3. Change the topic, 4.B',
'Ch2Choice1': 'What should I do?: 1. Wake up Bob to help find Jim, 2. Look for Jim alone, 3. Wake everyone up to help find Jim, 4.C',
'Ch2Choice2': 'What should I do?: 1. Take lantern, 2. Leave lantern, 3.C',
'Ch3Choice1': 'Should I: 1. Let Hill use explosives, 2. Don\'t let Hill use his explosives, 3.C' 
}
		
# append all story (list for each branch of story)
# get player name first before appending 
playerName = raw_input("Enter player name:" )
story = []
chapter1 = []
chapter1Part2 = []
chapter1BranchA = []
chapter1BranchB = []
chapter1BranchC = []
chapter2 = []
chapter2BranchA = []
chapter2BranchB = []
chapter2BranchC = []
chapter2TakeLantern = []
chapter2DontTakeLantern = []
chapter3BobAlivePart1 = []
chapter3BobAlivePart2 = []
chapter3BobAlivePart3 = []
chapter3CodyAlivePart1 = []
chapter3TannerAlivePart1 = []
chapter3HillAlivePart1 = []
chapter3UseHillExp = []
chapter3DonUseExp = []


# chapter1
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
chapter1.append('''You feel a little excited as well as terrified knowing by this time tomorrow you\'ll be outside on the surface being able to look at the sky.''')
chapter1.append('''You begin making your way to just outside the exit of this underground city.''')
chapter1.append('''There the expedition leader will be waiting as well as everyone else going to the surface.''')
chapter1.append('''You arrive at the meeting point, you quite a few people here at least for a run to the outside. Including your long time friend Bob, who comes over to you to greet you.''')
chapter1.append('''Bob: “Hey, ''' + playerName + ''' I hope you got everything packed. Seems quite a few more people are going this time around than previous times. I guess it’s because this will be the first time humanity is going all the way to the surface rather than just digging holes that might reach the surface.” ''')
chapter1.append(playerName + ''': "Yeah seems like it. I think everything should go smoothly. The last diggers said that they\'ve finally made a path all the way to the sewers of the surface.Though they stopped in fear of the radiation up there."''')
chapter1.append('''Bob: "True, but today is different. Today they said they\'ll have radiation suits to help protect us from the radiation. Though I wonder where they even found the suits.”''')
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
chapter1.append('''Joule: "The earthquakes may have caused some rocks to block our path forwards, but it\'s nothing we can\'t manage. If the rubble is too much we will have to reschedule this expedition. That however is an absolute last resort. ''')
chapter1.append('''Joule: “Everyone suit up and get ready! We head out in 10 minutes!” ''')
chapter1.append('''Jim: "Hey,'''+playerName+'''..."''')
chapter1.append('''I\'ve only met Jim once and that was on an expedition not to long ago. We went south when a cave in occurred blocking my way back. Luckily, Jim was there and was able to make his way over to me. The speed of his digging got me out before I even realized that I was trapped ''')
chapter1.append('''Bob: "What do you think he wants ''' +playerName+'''?''')
chapter1.append('''I looked over to Bob and shook my head ''')
chapter1.append(playerName +''': “I don’t know. I’ll go see what he wants”  ''')
chapter1.append('''I walk over to Jim ''')
chapter1.append(playerName+ ''': "Hey Jim, something you want to tell me? ''')
chapter1.append('''Jim gave me a hard look in the eyes and whispered to me ''')
chapter1.append('''Jim: “Don\'t trust Joule…” ''')
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


# chapter1BranchA decide to tell bob what Jim said 
chapter1BranchA.append('''You decide to tell Bob everything Jim told you. Bob understandably looks worried.''')
chapter1BranchA.append('''Bob:"I\'m not sure what to make of all of that. We well stay on alert and watch each other\'s backs. I really hope he is wrong though."''')
chapter1BranchA.append(playerName + ''':"We can just keep this between the three of us. We don\'t want to cause any issues in case what Jim said is wrong. We will stay on the lookout though."''')

# chapter1BranchB don't tell Bob what Jim said (lie)
chapter1BranchB.append('''You decude to lie to Bob.''')
chapter1BranchB.append(playerName + ''':"Jim was just asking if we prepared everything we needed for the trip."''')
chapter1BranchB.append('''Bob doesn't seem to fully believe you.''')
chapter1BranchB.append('''Bob: "Ok whatever you say. It must have been very important if you feel the need to keep it away from me."''')
chapter1BranchB.append('''"Bob didn't buy the lie. I don't really have a choice though. Telling him now would cause unessesary conflict."''')
chapter1BranchB.append(playerName + ''':"That was he really all he asked."''')
chapter1BranchB.append('''Bob: "Ok whatever let\'s just finish getting ready."''')

# chapter1BranchC change the topic 
chapter1BranchC.append(playerName + ''': "It wasn't anything worth metioning. More importantly we should finish preparing before Joule gets angry. The surface is within reach"''')
chapter1BranchC.append('''Bob: "Right we should finish up. Just a few more obstacles and we can finally reach the surface."''')
chapter1BranchC.append(playerName + ''': "These obstacles are nothing to us. We will overcome them easily and reach our goal."''')
chapter1BranchC.append('''Bob: "Yeah, well will be there shortly! Let\'s get our stuff together."''')
chapter1BranchC.append('''"Good. Bob only has his sights on reaching the surface.I won\'t need to worry about him asking about Jim."''')


# chapter 1 part 2
chapter1Part2.append('''Just as we are finishing packing Joule begins to wave and speak loudly to get our attention''')
chapter1Part2.append('''Joule: “Ok everyone seems like we are ready to go so let us begin.” ''')
chapter1Part2.append('''We begin heading into the first passage. The path will slowly elevate us upwards until we reach the resting post. We set up there and continue our journey the next day. It should take us roughly 4 days to reach the sewers. We should be able to reach a resting post each day until we finally reach the surface. ''')
chapter1Part2.append('''As we approach the first resting post, I realize that Cody\'s breathing is irregular, almost anxious. It could just be nerves getting to him, but what Jim told me still weighs heavily in my mind. ''')
chapter1Part2.append('''Come to think of it I\'ve never been on an expedition with Cody before. I’ve only ever encountered him around the city. I have been told about his expeditions before, but never anything in detail. ''')

# chapter 2
chapter2.append('''After a long day traveling through the underground we come to a stop. It\'s time for our rest. ''')
chapter2.append('''Joule: “Alright everyone we are setting up here for the night. It’s a bit early for a rest stop, but the next closest rest site is too far to travel to in one day. Get all the rest you can because the next stop will take longer to reach.” ''')
chapter2.append('''As everyone begins to pick out their sleeping spots, Jim and I decide to sleep close in case Joule tries anything (Maybe we can add Bob depending if the player told bob or not). I take one last look around and fall asleep. ''')
chapter2.append(''' *dreaming of reaching the surface* ''')
chapter2.append('''I wake up to a horrific nose. As I look around I notice that Jim is gone. He might have gotten up to use the bathroom or something, but can\'t be too sure about that. ''')
chapter2.append('''So, I decide to stay up for a bit and wait for Jim to come back. A few minutes pass and Jim isn\'t back yet. I take a closer look around and also notice that Joule is gone as well. This isn\'t good. I get up and look for Jim. ''')
chapter2.append('''(Ch2Choice1) ''')

# chapter2BranchA wake up Bob
chapter2BranchA.append(playerName + ''': Hey Bob wake up.''')
chapter2BranchA.append('''You quickly explain to Bob that Jim is missing.''')
chapter2BranchA.append('''Bob agrees to help you look for Jim.''')
chapter2BranchA.append('''Bob points over to the lantern sugguesting we take it with us to help light the way.''')
chapter2BranchA.append('''(Ch2Choice2) ''')

# chapter2BranchB look for jim alone
chapter2BranchB.append('''It\' nearly pitch black except for the small glow radiating from the lantern in the middle of everyone sleeping.''')
chapter2BranchB.append('''"It would be great to take it with me, but I risk waking up someone."''')
chapter2BranchB.append('''"I don’t want to deal with anyone\'s questions right now either."''')
chapter2BranchB.append('''(Ch2Choice2) ''')

# chapter 2 decide to take lantern 
# Hill, Yuma, Cody dies
chapter2TakeLantern.append('''You take the lantern and start making your way out of the camp, leaving the camp without any light.''')
chapter2TakeLantern.append('''It didn't take very long for you to start smelling something incredibly foul.''')
chapter2TakeLantern.append('''It's then that you find Jim.''')
chapter2TakeLantern.append('''Jim is on the floor eviscerated. The only way you are able to identify that it is him is by the pieces of clothing left behind. That\'s definitely Jim.''')
chapter2TakeLantern.append('''You grab your stomach and suddenly a rush of vomit spews out of your mouth.''')
chapter2TakeLantern.append('''After you regain your composure you come to the realization that Jim is dead. You decide to hurry back to tell everyone the fate that has befallen Jim.''')
chapter2TakeLantern.append('''Just then you hear screams coming back from camp.''')
chapter2TakeLantern.append('''You start to run back to camp. Something must be wrong.''')
chapter2TakeLantern.append(playerName + ''':"Oh no! Did the killer make their way to camp!?"''')
chapter2TakeLantern.append('''As you reach the camp you were horrified at the sight.''')
chapter2TakeLantern.append(playerName + ''':"No...''')
chapter2TakeLantern.append('''The only thing before you are torn bits of flesh and a massive amount of blood.''')
chapter2TakeLantern.append('''Something else eventualy catches your sight. Something living.''')
chapter2TakeLantern.append('''All around the bloody scene humanoid creatures. Luckily they haven\'t spotted you as they are to busy tearing and eating your fellow crew mates.''')
chapter2TakeLantern.append('''You slowly drop the lantern as to not give away your position and slowly turn to leave. However, just as you turn around you notice that a creature was just second away from getting the jump on you. The only hope for survival now is to stand and fight.''')
chapter2TakeLantern.append('''(Battle:mutant)''')

# chpater 2 decide to not take lantern
# Yuma dies 
chapter2DontTakeLantern.append('''You decide to leave the lantern where it is.''')
chapter2DontTakeLantern.append('''as you leave the camp you begin to smell something most foul.''')
chapter2DontTakeLantern.append('''Since your walking in complete darkness it\'s hard for you see anything and to pin point where the smell is coming from.''')
chapter2DontTakeLantern.append('''After walking for some time you trip over something and almost fall to the floor.''')
chapter2DontTakeLantern.append('''Just then you hear someone yelling coming back from the camp.''')
chapter2DontTakeLantern.append('''"Everyone wake up! theres something here!"''')
chapter2DontTakeLantern.append('''You start to rush back to camp without really thinking.''')
chapter2DontTakeLantern.append('''Once you get closer to the camp you notice everyone running back in your direction and going past you.''')
chapter2DontTakeLantern.append('''Back at the camp you can see someone getting shreded and torn to bits.''')
chapter2DontTakeLantern.append('''In the heat of the moment you don\'t hesitate to stay any longer.''')
chapter2DontTakeLantern.append('''As you turn around to start following everyone you notice that a creature was just second away from getting the jump on you!''')
chapter2DontTakeLantern.append('''At this point you're not sure what to do but fight to stay alive''')
chapter2DontTakeLantern.append('''(Battle:mutant)''')

# chapter2BranchC wake everyone up to find jim 
chapter2BranchC.append('''You decide to wake eveyone up.''')
chapter2BranchC.append(playerName + ''': "Get up everyone! Jim and Joule are missing!''')
chapter2BranchC.append('''Tanner: "Who cares! They probably just needed to take a piss. Just shut up and let us sleep.''')
chapter2BranchC.append(playerName + ''':I don't think that\'s it. They\'ve been gone for a while now. We really should go look for them.''')
chapter2BranchC.append('''Cody: "I agree with '''+playerName+'''. I noticed that they left one after the other. Quite some time has passed and they still aren\'t back.''')
chapter2BranchC.append('''Tanner: "Alright fine! Let's hurry up and find them already. You can apologize for waking me up afterwards. Wake up Yuma!"''')
chapter2BranchC.append('''Yuma: "...huh? What's going on? Why did you wake me up?" ''')
chapter2BranchC.append('''Tanner: " Just get up and help look for Joule and Jim. '''+playerName+''' and Cody think they are in trouble, but I\'m sure they are overthinking it. The faster we bring them back the faster we can prove '''+playerName+''' and Cody are wrong and we can go back to sleep.''')
chapter2BranchC.append('''Just then a rush of howls and screams start to come from all around the camp''')
chapter2BranchC.append('''Creatures start to come out of the dark into the camp\'s light and start attacking''')
chapter2BranchC.append('''You have no choice but to fight!''')
chapter2BranchC.append('''(Battle:mutant)''')

# chapter3 if Bob is alive part 1
chapter3BobAlivePart1.append('''Bob: “I didn’t really get a good look at them but the smell… it was terrible. Like something rotting."''')
chapter3BobAlivePart1.append('''Bob: One minute we were looking for Joule and Jim then the next minute Yuma\’s head was just… gone.”''')
chapter3BobAlivePart1.append('''Bob: “I didn’t even see what took it…”''')

# chpater3 if Bob is alive part 2
chapter3BobAlivePart2.append(playerName + ''': “This is my fault. I caused this.”''')
chapter3BobAlivePart2.append('''Bob: “This is not your fault. Those things would have attacked regardless if we were awake or asleep. We wouldn’t be alive if it weren’t for you.”''') 

# chpater3 if Bob is alive part 3
chapter3BobAlivePart3.append(playerName + ''': “I guess things could have been worse… We should keep moving. There might be more of those things around.”''') 
chapter3BobAlivePart3.append('''Bob: “Right let\ ’s go.”''')
chapter3BobAlivePart3.append('''The party continues to make their way through the dark tunnel. Without a primary light source they are forced to rely on a few matches that they have. Their supply is dwindling.''') 
chapter3BobAlivePart3.append('''They eventually come up on an elevator that was built the same time the underground city was built.''')
chapter3BobAlivePart3.append('''It was meant to be a convenient way for people to come and go from the underground city to the surface.''')
chapter3BobAlivePart3.append('''However, the blasts on the surface caused a lot of cave ins.''')
chapter3BobAlivePart3.append('''Because the construction of the tunnels wasn’t fully done, they couldn’t withstand the impacts and shocks of the explosions. This is what lead to the creation of the expedition teams to dig a path back to the surface.''')
chapter3BobAlivePart3.append('''Bob: “This elevator will take us up all the way to the sewers. From there it won\’t take us long to reach the surface.”''')
chapter3BobAlivePart3.append(playerName + ''': “Awesome, but where is the elevator?”''')
chapter3BobAlivePart3.append('''Bob: “The elevator should still be down here. The last expedition team used it to come back to underground city. There shouldn’t be anyone else using the elevator besides us…”''')
chapter3BobAlivePart3.append(playerName + ''': “Do you think someone survived the attack and somehow got ahead of us?”''')
chapter3BobAlivePart3.append('''Bob: “I don\’t know, but let’s try to bring it down. There is a crank we need to turn. It takes a few minutes to power up the elevator.”''')
chapter3BobAlivePart3.append(playerName + ''': “Alright. Let’s get to work!”''')
chapter3BobAlivePart3.append('''Bob: “Ok. I\’ll start cranking. Keep an eye out in case those things come back.”''')
chapter3BobAlivePart3.append(playerName + ''': “Right.”''')
chapter3BobAlivePart3.append('''As Bob turns the crank it begins to make a loud noise. It sounds like old rusted gears turning.The noise echoes loudly throughout the area. Bob and playerName look at each other and quickly realize that those monsters are probably headed their way because of the noise. Bob rushes to turn the crank faster to try and speed up the process.''')
chapter3BobAlivePart3.append('''In the distance you begin to hear someone screaming in the distance. Bob continues to turn the crank.''')

# chapter 3 if Cody is alive part 1
chapter3CodyAlivePart1.append('''Cody: “Whatever they where they couldn't have been human they looked to deformed.”''')

# chpater 3 if Tanner is alive part 1
chapter3TannerAlivePart1.append('''Tanner: “Yeah don\'t feel bad with my gun here they’ll be no problems when it comes down to dealing with those beasts will make it to the surface no problem now that I know there is something out there I won’t let it get to us so easily.” ''')

# chapter 3 if Hill is alive part 1
chapter3HillAlivePart1.append('''Hill: “Right it\’s my time to shine! Don\’t worry I have an idea! I\’ll just set down some charges right over here.”''')
chapter3HillAlivePart1.append('''Hill runs toward the screams then stops about 50 feet from the elevator''')
chapter3HillAlivePart1.append('''Hill begins placing charges on both sides of the wall of the cave.''')
chapter3HillAlivePart1.append('''Hill: “Ok that should be good!”''')
chapter3HillAlivePart1.append('''Tanner: “What are you planning on doing??''')
chapter3HillAlivePart1.append('''Hill: “Saving our lives! This will stop them in their tracks before getting to us.”''')
chapter3HillAlivePart1.append(''''Tanner: “But isn\’t there a chance we could also be caved in with them??”''')
chapter3HillAlivePart1.append('''Hill: “That’s a chance I\’m willing to take. If they get to us there is no way we\’ll make it out of here alive. Just trust me on this!”''')
chapter3HillAlivePart1.append('''Tanner: "''' + playerName + ''' you aren't really gonna let Hill kill us are you???”''')
chapter3HillAlivePart1.append('''Cody: “I\’d rather take my chances with the explosion than getting torn up by those monsters.”''')
chapter3HillAlivePart1.append('''(Ch3Choice1)''')

# let hill use explosives Hill and Cody lives 
chapter3UseHillExp.append('''Hill uses explosives mutants can\'t get in''')
chapter3UseHillExp.append('''Cody: “I won\'t let you fight them on your own!”''')
chapter3UseHillExp.append('''Cody joins in the fray and begins firing his pistol.''')
chapter3UseHillExp.append('''(Battle:mutant)''')
chapter3UseHillExp.append('''They put up a fight and are able to keep them at bay long enough for the elevator to come down. I quickly get inside and yell to Bob.''')
chapter3UseHillExp.append(playerName + ''': “Hurry! Get in! The elevators here!”''')

# don't let hill use explosives Hill & Cody dies 
chapter3DonUseExp.append('''Hill doesn\'t use explosives''')
chapter3DonUseExp.append('''The more Bob turns the crank the louder the screams get.''')
chapter3DonUseExp.append('''You can feel your heart pounding. You just want to run and hide, but the only place to go is back where the screams are coming from.''')
chapter3DonUseExp.append('''As the screams get louder so do the gears. Bob is pushing himself to turn the crank as fast as he possibly can.''')
chapter3DonUseExp.append('''Just as the crank stops turning you hear a generator turning on. A small low lit light come on.''')
chapter3DonUseExp.append('''The console for the elevator is now lit. Bob quickly presses the call button.''')
chapter3DonUseExp.append('''Both you and Bob turn and face the direction that the screams are coming from.  It\'s pitch black and you can’t make anything out.''')
chapter3DonUseExp.append('''You look up and you can barely see what you think is the elevator coming down.''')
chapter3DonUseExp.append('''Then you hear a scream. It sounds like they are only a few feet away from you.''')
chapter3DonUseExp.append('''You begin to smell a rotten odor that makes you want to vomit, but you\'re too scared to.''')
chapter3DonUseExp.append('''Finally they reach you. You can  almost see them clearly. They look human, but their flesh is green, bubbly, and falling off. Their eyes are gone and some still have them dangling out of their sockets. Some are missing their limbs. Their mouth dripping with blood and other body fluids.''')
chapter3DonUseExp.append('''You think to yourself “this is it. It’s over.”''')
chapter3DonUseExp.append('''But just then Bob looks toward you and says''')
chapter3DonUseExp.append('''Bob: “It\'s been an honor to have been by your side for so long, but I won\'t let them take you like they’ve taken everyone else”''')
chapter3DonUseExp.append('''Bob pulls out a small knife and runs between those mutants.''')
chapter3DonUseExp.append('''Bob begins fighting off the mass horde of mutations.''')


# Hill dies

DisplayStory(chapter1)
DisplayStory(chapter1Part2)
DisplayStory(chapter2)
branchThis()