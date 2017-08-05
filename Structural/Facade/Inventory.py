class Inventory:

    def __init__(self, max_capacity):
        self.max_capacity = max_capacity
        self.occupied_capacity = 0
        self.items = list()

    def get_inventory(self):
        inventory = {
            'items': self.items,
            'occupied_capacity': self.occupied_capacity,
            'max_capacity': self.max_capacity
        }
        return inventory

    def check_if_full(self, weight):
        if (self.max_capacity - self.occupied_capacity) >= weight:
            return True
        return False

    def add_item(self, item):
        self.items.append(item)
        self.increase_occupied_capacity(item.get_weight())

    def increase_occupied_capacity(self, weight):
        self.occupied_capacity += weight

