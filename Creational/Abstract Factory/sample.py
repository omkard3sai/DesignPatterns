from AbstractFactory import RoomFactory

# Create fire room and trap
print("Generating fire room....")
newfirefactory = RoomFactory.generateroom("Fire")

# Create ice room and trap
print("Creating ice room....")
newicefactory = RoomFactory.generateroom("Ice")
