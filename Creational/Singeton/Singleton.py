class FinalRoom:

    class __RoomData:
        def __init__(self, room_type):
            self.room_type = room_type
    instance = None

    def __init__(self, room_type):
        if FinalRoom.instance is None:
            FinalRoom.instance = FinalRoom.__RoomData(room_type)
            print("-> Created singleton object with " + str(FinalRoom.instance.room_type))
        else:
            old_room_type = FinalRoom.instance.room_type
            FinalRoom.instance.room_type = room_type
            print("-> Rewrote " + str(old_room_type) + " with " + str(FinalRoom.instance.room_type))

    @staticmethod
    def get_data():
        return FinalRoom.instance.room_type


