class Trap:

    @staticmethod
    def createtrap(traptype=None):
        if traptype == "Ice":
            return IceTrap()
        if traptype == "Fire":
            return FireTrap()


class IceTrap:

    def __init__(self):
        print("Ice trap created")


class FireTrap:

    def __init__(self):
        print("Fire trap created")
