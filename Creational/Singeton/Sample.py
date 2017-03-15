from DesignPatterns.Creational.Singeton.Singleton import Singleton

# Try to create first object
print("Trying to create first object")
firstobject = Singleton('Object1')

# Try to create second object
print("Trying to create second object")
secondobject = Singleton('Object2')

# Print both objects
print("Printing data from first object")
print("-> Object data :: " + str(firstobject.getdata()))
print("Printing data from second object")
print("-> Object data :: " + str(secondobject.getdata()))


