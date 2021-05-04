# cs472_battleshipAI
Term Project for CS 472. Building an AI to play the board game Battleship

Credit to: Steven Navarro, Garrett Owen, Nick Fryer, and Andrew Ferdenzi

# Battleship game class information
## Ship Information
The following is how the game class identifies each individual ship. This is a reference to use while coding.

class index of ship : common name of ship : ship length 
0:Carrier:5
1:Battleship:4
2:Cruiser:3
3:Submarine:3
4:Destroyer:2

## Class variables
Below is a list of all class variables that are used and modified throughout execution. 

	self.p1ShipMap: Player 1's ship map
	self.p2ShipMap: Player 2's ship map
	self.p1ShotMap: Player 1's shot map
	self.p2ShotMap: Player 2's shot map

	self.p1CarrierHealth = 5 	: Player 1 Carrier Health, initialized at 5 at beginning of game 
	self.p1BattleshipHealth = 4 : Player 1 Battleship Health, initialized at 4 at beginning of game 
	self.p1CruiserHealth = 3	: Player 1 Cruiser Health, initialized at 3 at beginning of game 
	self.p1SubmarineHealth = 3	: Player 1 Submarine Health, initialized at 3 at beginning of game 
	self.p1DestroyerHealth = 2	: Player 1 Destroyer Health, initialized at 2 at beginning of game 

	self.p2CarrierHealth = 5	: Player 2 Carrier Health, initialized at 5 at beginning of game 
	self.p2BattleshipHealth = 4 : Player 2 Battleship Health, initialized at 4 at beginning of game 
	self.p2CruiserHealth = 3	: Player 2 Cruiser Health, initialized at 3 at beginning of game 
	self.p2SubmarineHealth = 3	: Player 2 Submarine Health, initialized at 3 at beginning of game 
	self.p2DestroyerHealth = 2	: Player 2 Destroyer Health, initialized at 2 at beginning of game 

	self.carrierSym = "A"	: Carrier symbol
	self.battleshipSym = "B": Battleship symbol
	self.cruiserSym = "C"	: Cruiser sumbol
	self.submarineSym = "S"	: Submarine symbol
	self.destroyerSym = "D"	: Destroyer symbol
	self.hitMark = "!"		: Hit mark symbol
	self.missMark = "X"		: Miss mark symbol
	self.emptySpace = " "	: Empty space symbol

## Core game function pseudo code
### Place Ship
	Place ship(self, playerID, shipID, startLoc, endLoc):
		playerID = self.getPlayerID(playerID)
		startLoc = self.getTup(startLoc)
		endLoc = self.getTup(endLoc)
		startLoc, endLoc = self.swap(startLoc, endLoc)
		crds = self.getCrds(startLoc, endLoc)
		# Board check
		for crd in crds:
			# Check to see if space is open on board
			upCount
			exit("Cannot place <descriptive> already ship there")
		if upCount != ship size per shipID?
			exit("Ship ID does not meet index locations")
		for crd in crds:
			place on board

### Call Shot
	Call fire(self, playerID, fireLoc):
		playerID = self.getPlayerID(playerID)
		fireLoc = self.getTup(fireLoc)
		if playerID == player1:
			if p2ShipMap at fireLoc != empty:
				# get Ship type
				minus health on that ship
				print("Hit")
				p1shots taken ++
			else:
				mark miss on map
				print("Miss")
				p1shotsTaken ++
		Above but other player

### Print Ship Map
	printShip(self, playerID):
		playerID = self.getPlayerID(playerID)
		if playerID == p1:
			print(p1 shipmap)
		elif playerID == p2:
			print(p2 shipmap)

### Print Shot Map
	printShot(self, playerID):
		playerID = self.getPlayerID(playerID)
		if playerID == p1:
			print(p1 shotmap)
		elif playerID == p2:
			print(p2 shotmap)

## Helper function pseudo code
### Get Player ID
	getPlayerID(self, playerID):
		# Check all ways to get the player id 

### Swap Coordinates
	swap(self, startLoc, endLoc):
		# Swap so that we are always going down and to the right

### Get Coordinates
	getCrds(self, startLoc, endLoc):
		# Given two coords, in down and to the right fasion, build list of all tuples in between
		# Confirm that this will not send them off the board?

### Get Tuple
	getTup(self, loc):
		# Confirm that they are valid positions on the board
		# Return the position as a tuple
		# Must be able to take both alphanumeric (A7) and just numberic (0,6) 
