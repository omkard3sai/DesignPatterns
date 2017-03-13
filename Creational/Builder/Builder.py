class RoomBuilder:

    def __init__(self):
        self.roomtype = None
        self.doors = 0
        self.windows = 0
        self.traps = 0
        print("-> New room created")

    def setroomtype(self, roomtype):
        self.roomtype = roomtype
        print("-> Room type set to " + roomtype)

    def adddoor(self):
        self.doors += 1
        print("-> Added a door in the room")

    def addwindow(self):
        self.windows += 1
        print("-> Added a window in the room")

    def addtrap(self):
        self.traps += 1
        print("-> Added a trap in the room")

    def buildroom(self):
        print("-> Building the room")
        return Room(self)


class Room:

    def __init__(self, room):
        self.roomtype = room.roomtype
        self.doors = room.doors
        self.windows = room.windows
        self.traps = room.traps

    def displayroom(self):
        print(":::: Room Details ::::")
        print("Room Type :: " + str(self.roomtype))
        print("No. of Doors :: " + str(self.doors))
        print("No. of Windows :: " + str(self.windows))
        print("No. of Traps :: " + str(self.traps))
