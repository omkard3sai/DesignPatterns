from Rooms import Room
from Traps import Trap


class RoomFactory:

    @staticmethod
    def generateroom(roomtype=None):
        if roomtype == "Ice":
            return IceRoomFactory()
        if roomtype == "Fire":
            return FireRoomFactory()


class IceRoomFactory:

    def __init__(self):
        self.room = Room.createroom("Ice")
        self.trap = Trap.createtrap("Ice")


class FireRoomFactory:

    def __init__(self):
        self.room = Room.createroom("Fire")
        self.trap = Trap.createtrap("Fire")
