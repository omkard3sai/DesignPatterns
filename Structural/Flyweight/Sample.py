from Weapons import Bow, DualShotBow

basic_bow = Bow()
print('Firing fire arrow with basic bow....')
basic_bow.fire_arrow('Fire')

dual_shot_bow = DualShotBow()
print('Firing fire arrow with dual shot bow....')
dual_shot_bow.fire_arrow('Fire')
print('Firing ice arrow with dual shot bow....')
dual_shot_bow.fire_arrow('Ice')


