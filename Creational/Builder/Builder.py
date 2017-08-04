class RoomBuilder:

    def __init__(self):
        self.room_type = None
        self.doors = 0
        self.windows = 0
        self.traps = 0
        print("-> New room created")

    def set_room_type(self, room_type):
        self.room_type = room_type
        print("-> Room type set to " + room_type)

    def add_door(self):
        self.doors += 1
        print("-> Added a door in the room")

    def add_window(self):
        self.windows += 1
        print("-> Added a window in the room")

    def add_trap(self):
        self.traps += 1
        print("-> Added a trap in the room")

    def build_room(self):
        print("-> Building the room")
        return Room(self)


class Room:

    def __init__(self, room):
        self.room_type = room.room_type
        self.doors = room.doors
        self.windows = room.windows
        self.traps = room.traps

    def display_room(self):
        print(":::: Room Details ::::")
        print("Room Type :: " + str(self.room_type))
        print("No. of Doors :: " + str(self.doors))
        print("No. of Windows :: " + str(self.windows))
        print("No. of Traps :: " + str(self.traps))
