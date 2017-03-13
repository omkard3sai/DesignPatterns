import copy


class Room:

    def __init__(self):
        self.roomtype = None
        self.doors = 0
        self.windows = 0
        self.traps = 0
        print("-> New prototype room created")

    def cloneroom(self):
        print("-> New clone room created")
        return copy.deepcopy(self)

    def setroomtype(self, roomtype):
        self.roomtype = roomtype
        print("-> Set roomtype to " + str(roomtype))

    def setdoors(self, doors):
        self.doors = doors
        print("-> Set no. of doors to " + str(self.doors))

    def setwindows(self, windows):
        self.windows = windows
        print("-> Set no. of windows to " + str(self.windows))

    def settraps(self, traps):
        self.traps = traps
        print("-> Set no. of traps to " + str(self.traps))

    def displayroom(self):
        print(":::: Room Details ::::")
        print("Room Type :: " + str(self.roomtype))
        print("No. of Doors :: " + str(self.doors))
        print("No. of Windows :: " + str(self.windows))
        print("No. of Traps :: " + str(self.traps))
