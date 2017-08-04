class Item:

    def __init__(self, damage=0, armor=0):
        self.damage = damage
        self.armor = armor

    def get_damage(self):
        return self.damage

    def get_armor(self):
        return self.armor


class Sword(Item):
    def __init__(self):
        super().__init__(20, 0)


class Shield(Item):
    def __init__(self):
        super().__init__(5, 10)


class Helmet(Item):
    def __init__(self):
        super().__init__(0, 15)
