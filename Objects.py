#Build-in-objects
#What is an object
#In OOP , data or state and functionality appear together. The essential concepts to understand when working
#with objects are class instantiation (creating objects from classes) and dot syntax (the syntax for accessing an
#object’s attributes and methods). A class defines attributes and methods shared by its objects.
#Think of it as the technical drawing of a car model.
#The class can then be instantiated to create an instance. The instance, or
#object, is a single car built based on those drawings.

# Define a class for fancy defining fancy cars
class FancyCar():
    pass
print(type(FancyCar))

# Instantiate a fancy car
my_car = FancyCar()
print(type(my_car))

#You don’t need to worry about creating your own classes at this point. Just understand that each object is an
#instantiation of a class.

#Object Methods and Attributes
#Objects store data in attributes. These attributes are variables attached to the object or object class.
#Objects define functionality in object methods (methods defined for all objects in a class) and
#class methods (methods attached to a class and shared by all objects in the class), which are
#functions attached to the object.

#These functions have access to the object’s attributes and can modify and use the object’s data.
#To call an object’s method or access one of its attributes, we use dot syntax:

# Define a class for fancy defining fancy bikes

class FancyBike():
    #Add a class variable
    wheels = 2
    cylinder = 1
    engine = '330 cc'
    name = 'Jawa Bobber'
    #Add a method
    def driveFast(self):
        bike_speed = int(input("Enter your bike speed\n"))
        if bike_speed > 80:
            print("Driving so fast, Please slow down your bike")
        elif bike_speed == 0:
            print("Bike is at Zero speed")
        else:
            print("Driving on normal speed")

# Instantiate a fancy bike
my_bike = FancyBike()
#Access the class attribute
print('Wheels on my bike',my_bike.wheels)
print('Engine of my bike is of',my_bike.engine)
print('Cylinder of bike',my_bike.cylinder)
print('Name of my bike',my_bike.name)

#Invoke the method
my_bike.driveFast()

#So here our FancyBike class defines a method called driveFast and multiple attributes like name,wheels etc.
#When you instantiate an instance of FancyBike named my_bike , you can access the attribute and invoke the method using
#the dot syntax.




