from InventoryFacade import InventoryFacade
from Items import Sword, Shield, Potion

inventory_facade_object = InventoryFacade(10)
# Add sword to inventory
print('Adding sword to inventory....')
sword_item = Sword(4)
inventory_facade_object.add_to_inventory(sword_item)
# Add shield to inventory
print('Adding shield to inventory....')
shield_item = Shield(4)
inventory_facade_object.add_to_inventory(shield_item)
# Add potion to inventory
print('Adding potion to inventory....')
potion_item = Potion(1)
inventory_facade_object.add_to_inventory(potion_item)
# Add shield to inventory
print('Adding shield to inventory....')
shield_item = Shield(4)
inventory_facade_object.add_to_inventory(shield_item)
# Add potion to inventory
print('Adding potion to inventory....')
potion_item = Potion(1)
inventory_facade_object.add_to_inventory(potion_item)

print('Printing inventory....')
inventory_facade_object.display_inventory()
