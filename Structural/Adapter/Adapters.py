from Objects import Trap, Door


class ItemActivator:

    def __init__(self):
        if self.__class__.__name__ == 'ItemActivator':
            print('-> Static item created')

    def activate(self):
        print('-> No Action')


class TrapAdapter(ItemActivator):

    def __init__(self):
        super().__init__()
        self.trap_object = Trap()
        print('-> Trap object wrapped in TrapAdapter')

    def activate(self):
        self.trap_object.disarm_trap()


class DoorAdapter(ItemActivator):

    def __init__(self):
        super().__init__()
        self.door_object = Door()
        print('-> Door object wrapped in DoorAdapter')

    def activate(self):
        self.door_object.toggle_door()
