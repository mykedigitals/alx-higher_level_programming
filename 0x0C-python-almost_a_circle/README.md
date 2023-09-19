1. Base class
mandatory
Write the first class Base:

Create a folder named models with an empty file __init__.py inside - with this file, the folder will become a Python package

2. First Rectangle
mandatory
Write the class Rectangle that inherits from Base:

In the file models/rectangle.py
Class Rectangle inherits from Base
Private instance attributes, each with its own public getter and setter:


3. Validate attributes
mandatory
Update the class Rectangle by adding validation of all setter methods and instantiation (id excluded):

If the input is not an integer, raise the TypeError exception with the message: <name of the attribute> must be an integer. Example: width must be an integer



4. Area first
mandatory
Update the class Rectangle by adding the public method def area(self): that returns the area value of the Rectangle instance.


5. Display #0
mandatory
Update the class Rectangle by adding the public method def display(self): that prints in stdout the Rectangle instance with the character # - you don’t need to handle x and y here.



6. __str__
mandatory
Update the class Rectangle by overriding the __str__ method so that it returns [Rectangle] (<id>) <x>/<y> - <width>/<height>


7. Display #1
mandatory
Update the class Rectangle by improving the public method def display(self): to print in stdout the Rectangle instance with the character # by taking care of x and y
