class Room:

    @staticmethod
    def create_room(room_type=None):
        if room_type == "Ice":
            return IceRoom()
        if room_type == "Fire":
            return FireRoom()


class IceRoom:

    def __init__(self):
        print("-> Ice room created")


class FireRoom:

    def __init__(self):
        print("-> Fire room created")
