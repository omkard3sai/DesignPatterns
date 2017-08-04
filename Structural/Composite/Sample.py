from PlayerItems import PlayerItems
from Items import Sword, Shield, Helmet

player_items = PlayerItems()
sword_item = Sword(20, 0)
shield_item = Shield(5, 10)
helmet_item = Helmet(0, 15)
player_items.add_item(sword_item)
player_items.add_item(shield_item)
player_items.add_item(helmet_item)

player_items.display()
