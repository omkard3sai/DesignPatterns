from DesignPatterns.Creational.AbstractFactory.Rooms import Room
from DesignPatterns.Creational.AbstractFactory.Traps import Trap


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
