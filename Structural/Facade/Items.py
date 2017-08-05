class Item:

    def __init__(self, weight):
        self.weight = weight

    def get_weight(self):
        return self.weight


class Sword(Item):

    def __init__(self, weight):
        super().__init__(weight)


class Shield(Item):
    def __init__(self, weight):
        super().__init__(weight)


class Potion(Item):
    def __init__(self, weight):
        super().__init__(weight)
