class Singleton:

    class __Data:
        def __init__(self, data):
            self.data = data
    instance = None

    def __init__(self, data):
        if Singleton.instance is None:
            Singleton.instance = Singleton.__Data(data)
            print("-> Created singleton object with " + str(Singleton.instance.data))
        else:
            olddata = Singleton.instance.data
            Singleton.instance.data = data
            print("-> Rewrote " + str(olddata) + " with " + str(Singleton.instance.data))

    @staticmethod
    def getdata():
        return Singleton.instance.data

