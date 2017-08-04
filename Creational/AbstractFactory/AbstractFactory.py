from Rooms import Room
from Traps import Trap


class RoomFactory:

    @staticmethod
    def generate_room(room_type=None):
        if room_type == "Ice":
            return IceRoomFactory()
        if room_type == "Fire":
            return FireRoomFactory()


class IceRoomFactory:

    def __init__(self):
        self.room = Room.createroom("Ice")
        self.trap = Trap.createtrap("Ice")


class FireRoomFactory:

    def __init__(self):
        self.room = Room.createroom("Fire")
        self.trap = Trap.createtrap("Fire")
