from battleship import *

# Creating a game session from the battleship class
session = game()

numberOfGames = 1

#session.randomShot(numberOfGames)

# Print maps
#session.heatMapMode(numberOfGames, printMaps=True)

# Do not print maps
session.heatMapMode(numberOfGames, printMaps=False)