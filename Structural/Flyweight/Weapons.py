from Quiver import Quiver


class Bow:

    def __init__(self):
        self.quiver = Quiver()

    def fire_arrow(self, arrow_type):
        self.quiver.get_arrow(arrow_type)
        print('-> Fired one ' + str(arrow_type) + ' arrow')


class DualShotBow:

    def __init__(self):
        super().__init__()
        self.quiver = Quiver()

    def fire_arrow(self, arrow_type):
        for i in range(2):
            self.quiver.get_arrow(arrow_type)
        print('-> Fired two ' + str(arrow_type) + ' arrows')
