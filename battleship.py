import math
import random
import copy

class game:
	""" 
		It is expected that all AI will be the AI playing as P1 against a generated map as P2
	"""
	"""
	Ships
		0:Carrier:5
		1:Battleship:4
		2:Cruiser:3
		3:Submarine:3
		4:Destroyer:2
	"""

	def __init__(self):
		# Player maps
		self.p1ShipMap = [[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "]]
		self.p2ShipMap = [[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "]]
		self.p1ShotMap = [[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "]]
		self.p2ShotMap = [[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "]]

		# Ship health
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

		# Analytics values 
		self.p1ShotsTaken = 0
		self.p2ShotsTaken = 0

		# Map icons
		self.carrierSym = "A"
		self.battleshipSym = "B"
		self.cruiserSym = "C"
		self.submarineSym = "S"
		self.destroyerSym = "D"

		self.hitMark = "!"
		self.missMark = "X"
		self.emptySpace = " "

		self.player1 = "1"
		self.player2 = "2"


	###################################################################################################################
	# Core Game Functions
	###################################################################################################################
	def printShip(self, playerID):
		playerID = self.getPlayerID(playerID)

		if playerID == self.player1:
			for row in self.p1ShipMap:
				for char in row:
					print("|" + char, end = ' ')
					
				print("|", end = ' ')
				print()
		elif playerID == self.player2:
			for row in self.p2ShipMap:
				for char in row:
					print("|" + char, end = ' ')
				print("|", end = ' ')
				print()

	def printShot(self, playerID):
		playerID = self.getPlayerID(playerID)

		if playerID == self.player1:
			for row in self.p1ShotMap:
				for char in row:
					print("|" + char, end = ' ')
					
				print("|", end = ' ')
				print()
		elif playerID == self.player2:
			for row in self.p2ShotMap:
				for char in row:
					print("|" + char, end = ' ')
				print("|", end = ' ')
				print()

	def placeShip(self, playerID, shipID, startLoc, endLoc):
		# Getting the playerID
		playerID = self.getPlayerID(playerID)

		# Getting the tuples for the locations
		startLoc = self.getTup(startLoc)
		endLoc = self.getTup(endLoc)

		# Swapping for down -> right
		startLoc, endLoc = self.swap(startLoc, endLoc)
		
		# Getting all the coords
		crds = self.getCrds(startLoc, endLoc)
		
		# Player 1
		if playerID == self.player1:
			# Board check
			spaces = 0
			for crd in crds:
				if self.p1ShipMap[crd[0]][crd[1]] == self.emptySpace:
					spaces += 1
				else:
					print("Cannot place at (" + str(crd[0]) + ", " + str(crd[1]) +  ") already ship there")
					return False
			
			# Checking that the requested spaces size matches the ship
			if shipID == 0 and spaces != 5:
				exit("Request spaces for Carrier does not meet length of 5")
			if shipID == 1 and spaces != 4:
				exit("Request spaces for Battleship does not meet length of 4")
			if shipID == 2 and spaces != 3:
				exit("Request spaces for Cruiser does not meet length of 3")
			if shipID == 3 and spaces != 3:
				exit("Request spaces for Submarine does not meet length of 3")
			if shipID == 4 and spaces != 2:
				exit("Request spaces for Destroyer does not meet length of 2")			

			# Actually placing ship
			for crd in crds:
				if shipID == 0:
					self.p1ShipMap[crd[0]][crd[1]] = self.carrierSym
				if shipID == 1:
					self.p1ShipMap[crd[0]][crd[1]] = self.battleshipSym
				if shipID == 2:
					self.p1ShipMap[crd[0]][crd[1]] = self.cruiserSym
				if shipID == 3:
					self.p1ShipMap[crd[0]][crd[1]] = self.submarineSym
				if shipID == 4:
					self.p1ShipMap[crd[0]][crd[1]] = self.destroyerSym

		elif playerID == self.player2:
			# Board check
			spaces = 0
			for crd in crds:
				if self.p2ShipMap[crd[0]][crd[1]] == self.emptySpace:
					spaces += 1
				else:
					print("Cannot place at (" + str(crd[0]) + ", " + str(crd[1]) +  ") already ship there")
					return False
			
			# Checking that the requested spaces size matches the ship
			if shipID == 0 and spaces != 5:
				exit("Request spaces for Carrier does not meet length of 5")
			if shipID == 1 and spaces != 4:
				exit("Request spaces for Battleship does not meet length of 4")
			if shipID == 2 and spaces != 3:
				exit("Request spaces for Cruiser does not meet length of 3")
			if shipID == 3 and spaces != 3:
				exit("Request spaces for Submarine does not meet length of 3")
			if shipID == 4 and spaces != 2:
				exit("Request spaces for Destroyer does not meet length of 2")			

			# Actually placing ship
			for crd in crds:
				if shipID == 0:
					self.p2ShipMap[crd[0]][crd[1]] = self.carrierSym
				if shipID == 1:
					self.p2ShipMap[crd[0]][crd[1]] = self.battleshipSym
				if shipID == 2:
					self.p2ShipMap[crd[0]][crd[1]] = self.cruiserSym
				if shipID == 3:
					self.p2ShipMap[crd[0]][crd[1]] = self.submarineSym
				if shipID == 4:
					self.p2ShipMap[crd[0]][crd[1]] = self.destroyerSym

	def fire(self, playerID, fireLoc):
		# Getting the playerID
		playerID = self.getPlayerID(playerID)
		
		# Getting the fireLoc in a tuple
		fireLoc = self.getTup(fireLoc)

		# Player1 firing at Player2
		if playerID == self.player1:
			# If not empty => hit
			if self.p2ShipMap[fireLoc[0]][fireLoc[1]] != self.emptySpace:
				# Decremeting health of enemy ship
				if self.p2ShipMap[fireLoc[0]][fireLoc[1]] == self.carrierSym:
					self.p2CarrierHealth -= 1
				if self.p2ShipMap[fireLoc[0]][fireLoc[1]] == self.battleshipSym:
					self.p2BattleshipHealth -= 1
				if self.p2ShipMap[fireLoc[0]][fireLoc[1]] == self.cruiserSym:
					self.p2CruiserHealth -= 1
				if self.p2ShipMap[fireLoc[0]][fireLoc[1]] == self.submarineSym:
					self.p2SubmarineHealth -= 1
				if self.p2ShipMap[fireLoc[0]][fireLoc[1]] == self.destroyerSym:
					self.p2DestroyerHealth -= 1

				# Updating map
				self.p1ShotMap[fireLoc[0]][fireLoc[1]] = self.hitMark

				print("Hit!")

				# Updating shots taken
				self.p1ShotsTaken += 1	
			# Empty space
			else:
				# Updating map
				self.p1ShotMap[fireLoc[0]][fireLoc[1]] = self.missMark
	
				print("Miss")

				# Updating shots taken
				self.p1ShotsTaken += 1	
		# Player2 firing at Player1
		elif playerID == self.player2:
			# If not empty => hit
			if self.p1ShipMap[fireLoc[0]][fireLoc[1]] != self.emptySpace:
				# Decremeting health of enemy ship
				if self.p1ShipMap[fireLoc[0]][fireLoc[1]] == self.carrierSym:
					self.p1CarrierHealth -= 1
				if self.p1ShipMap[fireLoc[0]][fireLoc[1]] == self.battleshipSym:
					self.p1BattleshipHealth -= 1
				if self.p1ShipMap[fireLoc[0]][fireLoc[1]] == self.cruiserSym:
					self.p1CruiserHealth -= 1
				if self.p1ShipMap[fireLoc[0]][fireLoc[1]] == self.submarineSym:
					self.p1SubmarineHealth -= 1
				if self.p1ShipMap[fireLoc[0]][fireLoc[1]] == self.destroyerSym:
					self.p1DestroyerHealth -= 1

				# Updating map
				self.p2ShotMap[fireLoc[0]][fireLoc[1]] = self.hitMark

				print("Hit!")

				# Updating shots taken
				self.p2ShotsTaken += 1	
			# Empty space
			else:
				# Updating map
				self.p2ShotMap[fireLoc[0]][fireLoc[1]] = self.missMark
	
				print("Miss")

				# Updating shots taken
				self.p2ShotsTaken += 1	

	def clearBoard(self):
		# Resetting maps
		self.p1ShipMap = [[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "]]
		self.p2ShipMap = [[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "]]
		self.p1ShotMap = [[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "]]
		self.p2ShotMap = [[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "]]

		# Resetting health
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

		# Resetting analytic values 
		self.p1ShotsTaken = 0
		self.p2ShotsTaken = 0

	###################################################################################################################
	# AI Functions
	###################################################################################################################
	def genRandomMap(self):
		##################
		# Carrier
		##################
		# The first ship will always be able to be placed
		# Selection direction to point ship
		direction = random.randint(0,1)
		# Vertical
		if direction == 0:
			start = (random.randint(0, 5), random.randint(0, 9))
			end = (start[0] + 4, start[1])
		# Horizontal
		else:
			start = (random.randint(0, 9), random.randint(0, 5))
			end = (start[0], start[1] + 4)
		

		self.placeShip("2", 0, start, end)

		
		##################
		# Battleship
		##################
		battleshipPlaced = False
		while battleshipPlaced == False:
			# Selection direction to point ship
			direction = random.randint(0,1)
			# Vertical
			if direction == 0:
				start = (random.randint(0, 6), random.randint(0, 9))
				end = (start[0] + 3, start[1])
			# Horizontal
			else:
				start = (random.randint(0, 9), random.randint(0, 6))
				end = (start[0], start[1] + 3)

			ret = self.placeShip("2", 1, start, end)
			if ret == False:
				continue
			battleshipPlaced = True		

		##################
		# Cruiser
		##################
		cruiserPlaced = False
		while cruiserPlaced == False:
			# Selection direction to point ship
			direction = random.randint(0,1)
			# Vertical
			if direction == 0:
				start = (random.randint(0, 7), random.randint(0, 9))
				end = (start[0] + 2, start[1])
			# Horizontal
			else:
				start = (random.randint(0, 9), random.randint(0, 7))
				end = (start[0], start[1] + 2)
			
		
			ret = self.placeShip("2", 2, start, end)
			if ret == False:
				continue
			cruiserPlaced = True		

		##################
		# Submarine
		##################
		submarinePlaced = False
		while submarinePlaced == False:
			# Selection direction to point ship
			direction = random.randint(0,1)
			# Vertical
			if direction == 0:
				start = (random.randint(0, 7), random.randint(0, 9))
				end = (start[0] + 2, start[1])
			# Horizontal
			else:
				start = (random.randint(0, 9), random.randint(0, 7))
				end = (start[0], start[1] + 2)
	
			ret = self.placeShip("2", 3, start, end)
			if ret == False:
				continue
			submarinePlaced = True		

		##################
		# Destroyer
		##################
		destroyerPlaced = False
		while destroyerPlaced == False:
			# Selection direction to point ship
			direction = random.randint(0,1)
			# Vertical
			if direction == 0:
				start = (random.randint(0, 8), random.randint(0, 9))
				end = (start[0] + 1, start[1])
			# Horizontal
			else:
				start = (random.randint(0, 9), random.randint(0, 8))
				end = (start[0], start[1] + 1)

			ret = self.placeShip("2", 4, start, end)
			if ret == False:
				continue
			destroyerPlaced = True		

	def randomShot(self, numPlays):
		shots = 0
		
		possibleShots = [(0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),(0,9),(1,0),(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(1,7),(1,8),(1,9),(2,0),(2,1),(2,2),(2,3),(2,4),(2,5),(2,6),(2,7),(2,8),(2,9),(3,0),(3,1),(3,2),(3,3),(3,4),(3,5),(3,6),(3,7),(3,8),(3,9),(4,0),(4,1),(4,2),(4,3),(4,4),(4,5),(4,6),(4,7),(4,8),(4,9),(5,0),(5,1),(5,2),(5,3),(5,4),(5,5),(5,6),(5,7),(5,8),(5,9),(6,0),(6,1),(6,2),(6,3),(6,4),(6,5),(6,6),(6,7),(6,8),(6,9),(7,0),(7,1),(7,2),(7,3),(7,4),(7,5),(7,6),(7,7),(7,8),(7,9),(8,0),(8,1),(8,2),(8,3),(8,4),(8,5),(8,6),(8,7),(8,8),(8,9),(9,0),(9,1),(9,2),(9,3),(9,4),(9,5),(9,6),(9,7),(9,8),(9,9)]

		for x in range(numPlays):
			# Building the random map for this game
			self.genRandomMap()

			# Saving copy of possible shots
			thisGameShots = copy.copy(possibleShots)
			# While Player1 has not won
			while not self.checkWin("1"):
				# Picking random shot
				shotIndex = random.randint(0,len(thisGameShots) - 1)

				# Firing at that location
				self.fire("1", thisGameShots[shotIndex])

				# Removing that index from the possible shots
				thisGameShots.pop(shotIndex)

				# Incrementing shots
				shots += 1

				#self.printShot("1")
			# Game over, resetting board
			self.clearBoard()


		print(str(shots) + " total shots taken out of " + str(numPlays) + " games. Average shots per game " + str(shots/numPlays)) 



	###################################################################################################################
	# Utility Functions
	###################################################################################################################
	# Gets the playersID
	def getPlayerID(self, playerID):
		# If int, cast to string
		if isinstance(playerID, int):
			playerID = str(playerID)
		
		if len(playerID) != 1:
			exit("Illegal playerID. Valid options are 1, 2, \"1\", or \"2\"")

		if playerID != "1" and playerID != "2":
			exit("Illegal playerID. Valid options are 1, 2, \"1\", or \"2\"")

		return playerID

	# Ensures that we are always going down and to the right
	def swap(self, crd1, crd2):
		# Horizontal
		if crd1[0] == crd2[0]:
			pass
		# Vertical
		elif crd1[1] == crd2[1]:
			pass
		# Slant
		else:
			exit("Slanted ships not allowed")

		crd1Tot = crd1[0] + crd1[1]
		crd2Tot = crd2[0] + crd2[1]


		if crd1Tot > crd2Tot:
			temp = crd1
			crd1 = crd2
			crd2 = temp

		return(crd1, crd2) 

	# Given two coords, in down and to the right fasion, build list of all tuples in between
	def getCrds(self, startLoc, endLoc):
		if int(startLoc[1]) > 9 or int(startLoc[1]) < 0 or int(endLoc[1]) > 9 or int(endLoc[1]) < 0:
			exit("Requested coords are above the limit of 9")
		if int(startLoc[0]) > 9 or int(startLoc[0]) < 0 or int(endLoc[0]) > 9 or int(endLoc[0]) < 0:
			exit("Requested coords are above the limit of 9")	
		
		ret = []
		# Horizontal
		if startLoc[0] == endLoc[0]:
			# Appending first coordinate to list
			ret.append(startLoc)
			
			# Temp var to hold the incrementing coordinate
			temp = startLoc[1] + 1
			while temp < endLoc[1]:
				# Creating new coordinate
				new = (startLoc[0], temp)
				# Appening
				ret.append(new)
				# Iterating
				temp += 1

			# Appening last coordinate
			ret.append(endLoc)
		# Vertical
		elif startLoc[1] == endLoc[1]:
			# Appending first coordinate to list
			ret.append(startLoc)
			
			# Temp var to hold the incrementing coordinate
			temp = startLoc[0] + 1
			while temp < endLoc[0]:
				# Creating new coordinate
				new = (temp, startLoc[1])
				# Appening
				ret.append(new)
				# Iterating
				temp += 1

			# Appening last coordinate
			ret.append(endLoc)
		return ret

	# Confirm that they are valid positions on the board
	# Return the position as a tuple
	def getTup(self, crd):
		# Len has to be 2
		if len(crd) != 2:
			exit("A board coordinate must be two long. Example: (0,1) or (9,5)")
		

		# Getting the first value
		try:
			first = crd[0]
			
			if not isinstance(first, int):
				exit("Must use 0-9 for coordinate system")

			# If out of bounds for board
			if first < 0 or first > 9:
				exit("Map position " + str(crd[0]) + " out of bounds. Must be 0-9")
		except Exception as e:
			exit("getTup of first index failed")

		# Getting the num value
		try:
			num = crd[1]
		
			if not isinstance(first, int):
				exit("Must use 0-9 for coordinate system")
		
			# If out of bounds for board
			if num < 0 or num > 9:
				exit("Map position " + str(crd[1]) + " out of bound. Must be 0-9")

		except Exception as e:
			print(e)
			exit("getTup of second index failed")

		# Returning as tuple
		return (first, num)

	def checkWin(self, playerID):
		playerID = self.getPlayerID(playerID)

		if playerID == self.player1:
			if self.p2CarrierHealth == 0 and self.p2BattleshipHealth == 0 and self.p2CruiserHealth == 0 and self.p2SubmarineHealth == 0 and self.p2DestroyerHealth == 0:
				return True
			else:
				return False 
		elif playerID == self.player2:
			if self.p1CarrierHealth == 0 and self.p1BattleshipHealth == 0 and self.p1CruiserHealth == 0 and self.p1SubmarineHealth == 0 and self.p1DestroyerHealth == 0:
				return True
			else:
				return False
		else:
			return False

	

