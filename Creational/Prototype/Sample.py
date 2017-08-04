from Prototype import Room

# Create prototype room
print("Creating prototype room....")
prototype_room = Room()

# Clone prototype room
print("Cloning prototype room")
cloned_room = prototype_room.clone_room()

# Set cloned room type to fire
print("Setting room type of cloned room to fire....")
cloned_room.set_room_type("Fire")

# Change number of doors in cloned room
print("Changing number of doors in cloned room....")
cloned_room.set_doors(2)

# Change number of windows in cloned room
print("Changing number of windows in cloned room....")
cloned_room.set_windows(3)

# Change number of traps in cloned room
print("Changing number of traps in cloned room....")
cloned_room.set_traps(4)

# Display prototype room
print("\nDisplay prototype room....")
prototype_room.display_room()

# Display cloned room
print("\nDisplay cloned room....")
cloned_room.display_room()
