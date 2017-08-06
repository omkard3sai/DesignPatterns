class PlayerAura:

    def __init__(self):
        self.auras = list()

    def add_aura(self, aura_object):
        self.auras = aura_object.get_auras()
        self.auras.append(str(self.__class__.__name__))

    def get_auras(self):
        return self.auras

    def print_auras(self):
        print('Printing all auras')
        for aura in self.auras:
            print('-> ' + str(aura))


class FireAura(PlayerAura):

    def __init__(self, aura_object):
        super().__init__()
        self.add_aura(aura_object)


class IceAura(PlayerAura):

    def __init__(self, aura_object):
        super().__init__()
        self.add_aura(aura_object)


class WaterAura(PlayerAura):

    def __init__(self, aura_object):
        super().__init__()
        self.add_aura(aura_object)


class EarthAura(PlayerAura):

    def __init__(self, aura_object):
        super().__init__()
        self.add_aura(aura_object)
