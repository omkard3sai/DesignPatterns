from Items import Item


class PlayerItems:

    def __init__(self):
        self.items = list()

    def add_item(self, item=Item):
        self.items.append(item)

    def display(self):
        print('Total Damage = ' + str(self.get_damage()))
        print('Total Armor = ' + str(self.get_armor()))

    def get_damage(self):
        damage = 0
        for item in self.items:
            damage += item.get_damage()
        return damage

    def get_armor(self):
        armor = 0
        for item in self.items:
            armor += item.get_armor()
        return armor
