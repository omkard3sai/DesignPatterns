class RarityInterface:

    @staticmethod
    def init_rarity(rarity=None):
        if rarity == 'Elite':
            return Elite()
        if rarity == 'Legendary':
            return Legendary()
        return Common()


class Rarity:

    def __init__(self, multiplier=1):
        self.multiplier = multiplier

    def get_multiplier(self):
        return self.multiplier


class Common(Rarity):

    def __init__(self):
        super().__init__()


class Elite(Rarity):

    def __init__(self):
        super().__init__(5)


class Legendary(Rarity):

    def __init__(self):
        super().__init__(10)
