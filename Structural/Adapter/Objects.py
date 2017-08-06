class Door:

    def __init__(self):
        print('-> Door object created')
        self.closed = True

    def toggle_door(self):
        if self.closed:
            self.closed = False
            print('-> Door was opened')
        else:
            self.closed = True
            print('-> Door was closed')


class Trap:

    def __init__(self):
        print('-> Trap object created')
        self.armed = True

    def disarm_trap(self):
        if self.armed:
            self.armed = False
            print('-> Trap disarmed')
        else:
            print('-> Trap is already disarmed')
