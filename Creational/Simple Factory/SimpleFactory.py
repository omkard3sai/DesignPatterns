class Room:

    @staticmethod
    def createroom(roomtype=None):
        if roomtype == "IceRoom":
            return IceRoom()
        if roomtype == "FireRoom":
            return FireRoom()


class IceRoom:

    def __init__(self):
        self.roomtype = "Ice Room"

    def getroomtype(self):
        return self.roomtype


class FireRoom:

    def __init__(self):
        self.roomtype = "Fire Room"

    def getroomtype(self):
        return self.roomtype


newfireroom = Room.createroom("FireRoom")
print(newfireroom.getroomtype())
newiceroom = Room.createroom("IceRoom")
print(newiceroom.getroomtype())
