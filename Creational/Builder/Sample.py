from Builder import RoomBuilder

# Create new room
print("Creating new room....")
roombuilder = RoomBuilder()

# Set room type to fire
print("Setting room type to fire....")
roombuilder.setroomtype("Fire")

# Add a door
print("Adding a door....")
roombuilder.adddoor()

# Add a window
print("Adding a window....")
roombuilder.addwindow()

# Add two traps
print("Adding two traps....")
roombuilder.addtrap()
roombuilder.addtrap()

# Build and display room
print("Build and display room....")
newroom = roombuilder.buildroom()
newroom.displayroom()
