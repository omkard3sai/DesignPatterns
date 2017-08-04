from Adapters import ItemActivator, TrapAdapter, DoorAdapter


class InteractionInterface:

    @classmethod
    def interact(cls, item_activator_object=ItemActivator):
        print('Interacting using ' + str(item_activator_object.__class__.__name__) + '....')
        item_activator_object.activate()


# Interact with trap
trap_object = TrapAdapter()
InteractionInterface.interact(trap_object)
InteractionInterface.interact(trap_object)

# Interact with door
door_object = DoorAdapter()
InteractionInterface.interact(door_object)
InteractionInterface.interact(door_object)

# Interact with void item
item = ItemActivator()
InteractionInterface.interact(item)


