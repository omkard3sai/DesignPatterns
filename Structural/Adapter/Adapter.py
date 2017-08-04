from Window import Window
from Door import Door


class WindowAdapter:

    def __init__(self, window_object=Window):
        self.window_object = window_object

    def open_structure(self):
        self.window_object.open_window()


class DoorAdapter:

    def __init__(self, door_object=Door):
        self.door_object = door_object

    def open_structure(self):
        self.door_object.open_door()
