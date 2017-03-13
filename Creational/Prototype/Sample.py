from DesignPatterns.Creational.Prototype.Prototype import Room

# Create prototype room
print("Creating prototype room....")
prototyperoom = Room()

# Clone prototype room
print("Cloning prototype room")
clonedroom = prototyperoom.cloneroom()

# Set cloned room type to fire
print("Setting room type of cloned room to fire....")
clonedroom.setroomtype("Fire")

# Change number of doors in cloned room
print("Changing number of doors in cloned room....")
clonedroom.setdoors(2)

# Change number of windows in cloned room
print("Changing number of windows in cloned room....")
clonedroom.setwindows(3)

# Change number of traps in cloned room
print("Changing number of traps in cloned room....")
clonedroom.settraps(4)

# Display prototype room
print("\nDisplay prototype room....")
prototyperoom.displayroom()

# Display cloned room
print("\nDisplay cloned room....")
clonedroom.displayroom()
