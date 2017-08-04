from PlayerItems import PlayerItems
from Items import Sword, Shield, Helmet

player_items = PlayerItems()
sword_item = Sword()
shield_item = Shield()
helmet_item = Helmet()
player_items.add_item(sword_item)
player_items.add_item(shield_item)
player_items.add_item(helmet_item)

player_items.display()
