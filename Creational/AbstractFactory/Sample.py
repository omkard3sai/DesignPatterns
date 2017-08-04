from AbstractFactory import RoomFactory

# Create fire room and trap
print("Generating fire room....")
new_fire_factory = RoomFactory.generate_room("Fire")

# Create ice room and trap
print("Generating ice room....")
new_ice_factory = RoomFactory.generate_room("Ice")
