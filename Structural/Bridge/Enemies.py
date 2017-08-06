from Rarity import RarityInterface


class Enemy:

    def __init__(self, rarity=None, health_multiplier=1, damage_multiplier=1):
        self.rarity = RarityInterface.init_rarity(rarity)
        self.health_multiplier = self.rarity.get_multiplier() * health_multiplier
        self.damage_multiplier = self.rarity.get_multiplier() * damage_multiplier

    def display_enemy(self):
        print(str(self.__class__.__name__) + ' (' + str(self.rarity.__class__.__name__) + ')')
        print('-> Health Multiplier = ' + str(self.health_multiplier))
        print('-> Damage Multiplier = ' + str(self.damage_multiplier))


class Goblin(Enemy):

    def __init__(self, rarity):
        super().__init__(rarity, 1, 3)


class Troll(Enemy):

    def __init__(self, rarity):
        super().__init__(rarity, 2, 2)


class Giant(Enemy):

    def __init__(self, rarity):
        super().__init__(rarity, 3, 1)


