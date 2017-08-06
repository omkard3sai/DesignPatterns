from Arrows import ArrowMaker


class Quiver:

    def __init__(self):
        self.arrows = dict()

    def get_arrow(self, arrow_type):
        if (arrow_type not in self.arrows) or (self.arrows[arrow_type]):
            self.arrows[arrow_type] = ArrowMaker.make_arrow(arrow_type)
            print('-> Created ' + str(arrow_type) + ' arrow')


