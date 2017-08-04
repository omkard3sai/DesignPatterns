import copy


class Room:

    def __init__(self):
        self.room_type = None
        self.doors = 0
        self.windows = 0
        self.traps = 0
        print("-> New prototype room created")

    def clone_room(self):
        print("-> New clone room created")
        return copy.deepcopy(self)

    def set_room_type(self, room_type):
        self.room_type = room_type
        print("-> Set room_type to " + str(room_type))

    def set_doors(self, doors):
        self.doors = doors
        print("-> Set no. of doors to " + str(self.doors))

    def set_windows(self, windows):
        self.windows = windows
        print("-> Set no. of windows to " + str(self.windows))

    def set_traps(self, traps):
        self.traps = traps
        print("-> Set no. of traps to " + str(self.traps))

    def display_room(self):
        print(":::: Room Details ::::")
        print("Room Type :: " + str(self.room_type))
        print("No. of Doors :: " + str(self.doors))
        print("No. of Windows :: " + str(self.windows))
        print("No. of Traps :: " + str(self.traps))
