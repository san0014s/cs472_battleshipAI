# cs472_battleshipAI
Term Project for CS 472. Building an AI to play the boardgame Battleship

0:Carrier:5
1:Battleship:4
2:Cruiser:3
3:Submarine:3
4:Destroyer:2

Class Variables:
	self.p1ShipMap
	self.p2ShipMap
	self.p1ShotMap
	self.p2ShotMap

	self.p1CarrierHealth = 5
	self.p1BattleshipHealth = 4
	self.p1CruiserHealth = 3
	self.p1SubmarineHealth = 3
	self.p1DestroyerHealth = 2

	self.p2CarrierHealth = 5
	self.p2BattleshipHealth = 4
	self.p2CruiserHealth = 3
	self.p2SubmarineHealth = 3
	self.p2DestroyerHealth = 2

	self.carrierSym = "A"
	self.battleshipSym = "B"
	self.cruiserSym = "C"
	self.submarineSym = "S"
	self.destroyerSym = "D"

	self.hitMark = "!"
	self.missMark = "X"
	self.emptySpace = " "


Game Functions:
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

	printShip(self, playerID):
		playerID = self.getPlayerID(playerID)

		if playerID == p1:
			print(p1 shipmap)
		elif playerID == p2:
			print(p2 shipmap)

	printShot(self, playerID):
		playerID = self.getPlayerID(playerID)

		if playerID == p1:
			print(p1 shotmap)
		elif playerID == p2:
			print(p2 shotmap)

Helper Functions:
	getPlayerID(self, playerID):
		# Check all ways to get the player id 

	swap(self, startLoc, endLoc):
		# Swap so that we are always going down and to the right

	getCrds(self, startLoc, endLoc):
		# Given two coords, in down and to the right fasion, build list of all tuples in between
		# Confirm that this will not send them off the board?

	getTup(self, loc):
		# Confirm that they are valid positions on the board
		# Return the position as a tuple
		# Must be able to take both alphanumeric (A7) and just numberic (0,6) 