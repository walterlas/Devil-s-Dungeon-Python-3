## Devil's Dungeon     ##
## Try #3 for Python 3 ##
##                     ##
## This version mostly ##
## works.              ##
#########################


import random					# We need random numbers
from os import system, name		# So we can clear the screen

roomContents=[]
adjRoomsFlags=[]
roomContentFlags=[]
visitedRooms=[]

adjacentRooms=[]
for i in range(0,66):
	adjacentRooms.append(0)
for i in range(0,20):
	roomContentFlags.append(0)
for i in range(0,17):
	roomContents.append(0)
	adjRoomsFlags.append(0)
	visitedRooms.append(0)
	
numberRooms=16
playerLocation=1
playerDepth=1
oldDepth=0
playerGold=0
playerExp=0
playerSpeed=101
playerStrength=101
roomGold=0
monsterStrength=0
monsterSpeed=0
playerHit=0
monsterHit=0

def rnd():
	return(random.random())

def clearScreen():
	if name == 'nt':		# for Windows
		_ = system('cls')
	else:
		_ = system('clear')
	return
def checkContentFlags(a,b):
	c=roomContentFlags[a]*roomContentFlags[b]
	return(c)
	
def setRooms():		# Lines 40-140
	global adjacentRooms
	global roomContents
	global visitedRooms
	global roomContentFlags
	
	for i in range(0,65+1):
		adjacentRooms[i]=0	# Set all adjacent rooms to 0
	for i in range(1,numberRooms+1):	# 
		n=int(3*rnd()+1)	# n = 1 to 4
		if i==1:
			n=3
		for j in range(1,n+1):
			r=int(64*rnd()+1)	# r = 1 to 64
			while adjacentRooms[r] !=0:
				r=int(64*rnd()+1)
			adjacentRooms[r]=i
		roomContents[i]=int(524287*rnd())
		visitedRooms[i]=0
	roomContents[playerLocation]=1
	roomContents[1]=24576
	for i in range(1,19+1):
		roomContentFlags[i]=0
	return

def checkHazards():
	global adjacentRooms
	global roomContentFlags
	global playerSpeed
	global playerStrength
	
	if rnd()<.01:
		print("Tremor!")
		for i in range(1,20+1):
			adjacentRooms[i]=int(numberRooms*rnd()+1)
	if rnd()<.01:
		print("Tremor!")
		for i in range(1,20+1):
			adjacentRooms[i]=0
#	if roomContentFlags[1]*roomContentFlags[12]==1 and rnd()<.4:
		if checkContentFlags(1,12):
		print("You have been cursed by a demon!")
		playerSpeed=(.5*playerSpeed)
#	if roomContentFlags[9]*roomContentFlags[11]==1 and rnd()<.4:
		if checkContentFlags(9,11)
		print("You have been gassed!")
		playerStrength=int(.5*playerStrength)
	return

def decrementTest():
	global playerSpeed
	global playerStrength
	
	playerSpeed -= 1
	playerStrength -= 1
	if (playerSpeed <=0) or (playerStrength <=0):
		print("You're dead.")
		quit()
	return

def doAdjacentRooms():
	global adjRoomsFlags
	global adjacentRooms
	
	for i in range(1,numberRooms+1):
		adjRoomsFlags[i]=0
	for i in range(1,64+1):
		if playerLocation != adjacentRooms[i]:
			continue
		if (adjacentRooms[i+1] !=0 ) and (adjacentRooms[i+1] != playerLocation):
			adjRoomsFlags[adjacentRooms[i+1]]=1
		if (adjacentRooms[i-1] != 0) and (adjacentRooms[i-1] != playerLocation):
			adjRoomsFlags[adjacentRooms[i-1]]=1
	return
	
def doConvert():
	global roomContentFlags
	
	n=roomContents[playerLocation]
	for i in range(1,19+1):
		q=n//2
		roomContentFlags[i]=2*(n/2-q)
		n=q
	return

def showStatus():
	print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
	print(f'Gold: {playerGold}  Experience: {playerExp}  Depth: {playerDepth}')
	print(f"Speed: {playerSpeed}  Strength: {playerStrength}")
	doAdjacentRooms()
	doConvert()
	return
	
def doDemons():
#	if (roomContentFlags[1]*roomContentFlags[12] == 1):
	if checkContentFlags(1,12):
		print("Demons!")
	return

def doMonsters():
	print(f"Monster's Speed: {monsterSpeed}  Strength: {monsterStrength}")
#	if (roomContentFlags[1]*roomContentFlags[12] == 1):
	if checkContentFlags(1,2):
		print("Demons!")
#	if (roomContentFlags[9]*roomContentFlags[11] ==1):
	if checkContentFlags(9,11):
		print("Poisonous Gas!")
	return
	
def mDG():
	global monsterSpeed
	global monsterStrength
	
	if (roomContentFlags[2]==0):
		monsterSpeed=0
		doDemons()
		return
	if monsterPresent==1:
		doMonsters()
		return
	monsterStrength=playerDepth*(roomContentFlags[3]+2*roomContentFlags[4]+4*roomContentFlags[5]+playerDepth)
	monsterSpeed = playerDepth*(roomContentFlags[6]+2*roomContentFlags[7]+4*roomContentFlags[8]+playerDepth)
	print(f"Monster's Speed: {monsterSpeed}  Strength: {monsterStrength}")
	if (roomContentFlags[1]*roomContentFlags[12] == 1):
		print("Demons!")
	if (roomContentFlags[9]*roomContentFlags[11] ==1):
		print("Poisonous Gas!")
	return

def calcTreasure():
	global treasure
	
	if (roomContentFlags[10] != 1):
		treasure=0
		return
	treasure=roomContentFlags[11]+2*roomContentFlags[12]+4*roomContentFlags[13]+1
	print("Maximum Gold: "+str(treasure*playerLocation*playerDepth+1))
	return

def slidesDropoffs():
	global slideTo
	
	slideTo=roomContentFlags[15]+2*roomContentFlags[16]+4*roomContentFlags[17]+8*roomContentFlags[18]+1
	if slideTo > numberRooms:
		slideTo = 1
	if slideTo == 0:
		slideTo = 1
	if (roomContentFlags[14] != 0) and (slideTo != playerLocation):
		print(f'Slide to: {int(slideTo)}')
	if roomContentFlags[19]*roomContentFlags[13] == 1:
		print("Dropoff")
	return

def showMoves():
	available=0
	print("Move from "+str(playerLocation)+" to",end=" ")
	for i in range(1,numberRooms+1):
		if adjRoomsFlags[i]==1 and i != playerLocation:
			print(i,end=" ")
			available += 1
	print("\n",end="\n")
	if available == 0:
		print("There is no where to go, so you just go home.")
		quit()
	return

def canMove():
	a = False
	for i in range(1,numberRooms+1):
		if adjRoomsFlags[i] == 1 and i != playerLocation:
			a = True
	return(a)

def endGame():
	print(f'You found {playerGold} pieces of gold. Bye!')
	return

def useWand():
	global playerStrength
	global playerSpeed
	
	if rnd()<.4:
		print("The wand backfires!")
		playerStrength=int(.5*playerStrength)
		playerSpeed=int(.5*playerSpeed)
	else:
		print("The wand worked!")
		roomContents[playerLocation]=266240
	return		# should return to showStatus

def goFight():
	global playerSpeed
	global playerStrength
	global monsterSpeed
	global monsterStrength
	global monsterPresent
	global playerExp
	
	monsterPresent=1
	playerHit=int(rnd()*playerStrength)
	monsterHit=int(rnd()*monsterStrength)
	if playerHit>monsterStrength:
		playerHit=monsterStrength
	if monsterHit>playerStrength:
		monsterHit=playerStrength
	if rnd()*playerSpeed < rnd()*monsterSpeed:
		print("Monster attacks!")
		playerStrength = playerStrength - monsterHit
		monsterStrength = monsterStrength - int(.5*playerHit)
	else:
		print("You attack!")
		monsterStrength = monsterStrength - playerHit
		playerStrength = playerStrength - int(.5*monsterHit)
	playerExp = playerExp+(2*playerHit)
	if monsterStrength <= 0:
		print("The monster is dead!")
		roomContents[playerLocation]=roomContents[playerLocation]-2
		return
	else:
		print("The monster is still alive!")
	return

def doRun():
	global playerStrength
	
	if rnd()*playerSpeed > rnd()*monsterSpeed:
		print("You escaped!")
	else:
		print("The monster hit you!")
		playerStrength =-int(.2*monsterStrength)
	return

def getTreasure():
	global roomGold
	global playerExp
	global playerGold
	
	if treasure == 0:
		return
	roomGold=int(rnd()*treasure*playerLocation*playerDepth)+1
#	if (roomContentFlags[1]*roomContentFlags[12]==1) and rnd()<.4:
	if checkContentFlags(1,12) and rnd()<.4:
		print("A demon got your gold!")
		roomGold=0
	else:
		print(f'You found {roomGold} pieces of gold.')
		playerGold += roomGold
		roomContents[playerLocation]=roomContents[playerLocation]-512
	playerExp += roomGold
	return
	
def doTrade():
	global playerSpeed
	global playerStrength
	global playerExp

	keepLooping=True
	while keepLooping:
		print(f'Experience: {playerExp}  Speed: {playerSpeed}  Strength: {playerStrength}')
		trade=int(input("Add to Speed > "))
		if playerExp-trade < 0:
			print("You need more experience.")
		else:
			playerExp -= trade
			playerSpeed += trade
			keepLooping = False
	keepLooping=True
	while keepLooping:
		trade=int(input("Add to Strength > "))
		if playerExp-trade < 0:
			print("You need more experience.")
		else:
			playerExp -= trade
			playerSpeed += trade
			keepLooping = False
	return

def showRooms():
	global playerLocation
	oldLocation = playerLocation
	for k in range(1,numberRooms+1):
		if visitedRooms[k] != 1:
			continue
		else:
			print(str(k)+"--",end=" ")
			playerLocation = k
			doAdjacentRooms()
			for j in range(1,numberRooms+1):
				if adjRoomsFlags[j] == 1 and j != k:
					print(str(j),end=" ")
			print(" ")
	playerLocation = oldLocation
	return
	
gameLoop = True
clearScreen()

while gameLoop:
	if playerDepth != oldDepth:		# Only setRooms if a new game or player goes down a level
		setRooms()
		oldDepth = playerDepth
	
	checkHazards()
	decrementTest()
	showStatus()
	mDG()	
	calcTreasure()
	slidesDropoffs()
	showMoves()
	pm=int(input("Your move > "))
	clearScreen()

#### This section handles player actions ####

	if (pm == 99):			# If in room 1, exit game; otherwise use wand
		if playerLocation == 1:
			endGame()
			gameLoop=False
		else:
			useWand()
		continue
		
	if (pm == 88):			# Show visited rooms and adjacent rooms
		showRooms()
		continue
		
	if (pm == 0) and (playerLocation == 1): # If in room 1, trade exp for str/spd
		doTrade()
		continue
		
	if (pm < 0):	# Go to next level down
#		if roomContentFlags[19] and roomContentFlags[13]:
		if checkContentFlags(19,13):
			playerDepth = playerDepth + 1
			monsterPresent = 0
		else:
			print("There's no dropoff here.")
		continue
		
	if (pm==0) and (monsterStrength > 0):	# Should fight a monster
		goFight()
		continue
		
	if (pm != 0) or (playerLocation != 1):	# Grab treasure. Not sure why I did this
		getTreasure()
		
	if (pm > 0) and (pm < 88):		# Process moving to a different room
		if (monsterStrength > 0):
			doRun()
		if adjRoomsFlags[pm] == 1 or pm==slideTo:
			playerLocation = pm
			monsterPresent = 0
			playerExp =+ playerDepth
			visitedRooms[playerLocation]=1
#			continue
		else:
			print("That room is not adjacent to here.")
#			continue

	
	

