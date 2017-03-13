class Room:

    @staticmethod
    def createroom(roomtype=None):
        if roomtype == "Ice":
            return IceRoom()
        if roomtype == "Fire":
            return FireRoom()


class IceRoom:

    def __init__(self):
        print("-> Ice room created")


class FireRoom:

    def __init__(self):
        print("-> Fire room created")
