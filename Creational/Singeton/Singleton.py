class FinalRoom:

    class __RoomData:
        def __init__(self, roomtype):
            self.roomtype = roomtype
    instance = None

    def __init__(self, roomtype):
        if FinalRoom.instance is None:
            FinalRoom.instance = FinalRoom.__RoomData(roomtype)
            print("-> Created singleton object with " + str(FinalRoom.instance.roomtype))
        else:
            oldroomtype = FinalRoom.instance.roomtype
            FinalRoom.instance.roomtype = roomtype
            print("-> Rewrote " + str(oldroomtype) + " with " + str(FinalRoom.instance.roomtype))

    @staticmethod
    def getdata():
        return FinalRoom.instance.roomtype


