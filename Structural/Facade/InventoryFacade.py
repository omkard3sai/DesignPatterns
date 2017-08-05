from Inventory import Inventory
from Items import Item, Sword, Shield


class InventoryFacade:

    def __init__(self, max_capacity=0):
        self.inventory_object = Inventory(max_capacity)

    def add_to_inventory(self, item=Item):
        if self.inventory_object.check_if_full(item.get_weight()):
            self.inventory_object.add_item(item)
            print('-> ' + str(item.__class__.__name__) + ' added to inventory')
        else:
            print('-> Inventory full')

    def display_inventory(self):
        inventory = self.inventory_object.get_inventory()
        print('Capacity => '
              + str(inventory['occupied_capacity'])
              + '/'
              + str(inventory['max_capacity']))
        print(':: Items ::')
        for item in inventory['items']:
            print(item.__class__.__name__)
