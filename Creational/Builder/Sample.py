from DesignPatterns.Creational.Builder.Builder import RoomBuilder

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

# Build the room
print("Build the room....")
newroom = roombuilder.buildroom()

# Display the room
print("\nDisplay room....")
newroom.displayroom()
