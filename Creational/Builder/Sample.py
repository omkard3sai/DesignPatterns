from Builder import RoomBuilder

# Create new room
print("Creating new room....")
room_builder = RoomBuilder()

# Set room type to fire
print("Setting room type to fire....")
room_builder.set_room_type("Fire")

# Add a door
print("Adding a door....")
room_builder.add_door()

# Add a window
print("Adding a window....")
room_builder.add_window()

# Add two traps
print("Adding two traps....")
room_builder.add_trap()
room_builder.add_trap()

# Build the room
print("Build the room....")
new_room = room_builder.build_room()

# Display the room
print("\nDisplay room....")
new_room.display_room()
