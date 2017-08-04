from Singleton import FinalRoom

# Try to create first object
print("Trying to create first object")
first_object = FinalRoom('Room_1')

# Try to create second object
print("Trying to create second object")
second_object = FinalRoom('Room_2')

# Print both objects
print("Printing data from first object")
print("-> Object data :: " + str(first_object.get_data()))
print("Printing data from second object")
print("-> Object data :: " + str(second_object.get_data()))


