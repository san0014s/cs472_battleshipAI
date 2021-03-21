from battleship import *

session = game()

"""
session.placeShip("2", 0, (0,0), (0,4))
session.placeShip("2", 1, (1,0), (4,0))
session.placeShip("2", 2, (9,7), (9,9))
session.placeShip("2", 3, (8,7), (8,9))
session.placeShip("2", 4, (3,3), (3,4))
session.printShip("2")

session.fire("1", (0,0))
session.fire("1", (0,1))
session.fire("1", (0,2))
session.fire("1", (0,3))
session.fire("1", (0,4))
session.fire("1", (1,0))
session.fire("1", (2,0))
session.fire("1", (3,0))
session.fire("1", (4,0))
session.fire("1", (3,3))
session.fire("1", (3,4))
session.fire("1", (3,5))
session.fire("1", (8,7))
session.fire("1", (8,8))
session.fire("1", (8,9))
session.fire("1", (9,7))
session.fire("1", (9,8))
session.fire("1", (9,9))

session.printShot("1")


print(session.checkWin("1"))
"""
session.randomShot(1000)

#session.fire("1", (5,5))
#session.printShot("1")


#session.genRandomMap()
#session.printShip("2")