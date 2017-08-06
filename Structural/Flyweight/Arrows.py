class ArrowMaker:

    @staticmethod
    def make_arrow(arrow_type=None):
        if arrow_type == 'Fire':
            return FireArrow()
        if arrow_type == 'Ice':
            return IceArrow()
        return BasicArrow()


class BasicArrow:

    def __init__(self, arrow_type='Basic'):
        self.type = arrow_type

    def get_arrow_type(self):
        return self.type


class FireArrow(BasicArrow):

    def __init__(self):
        super().__init__('Fire')


class IceArrow(BasicArrow):

    def __init__(self):
        super().__init__('Ice')
