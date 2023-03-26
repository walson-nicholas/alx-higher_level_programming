#!/usr/bin/python3
<<<<<<< HEAD
"""Defines a rectangle class."""
=======
"""
    contains class Rectangle which implements Base.
"""
>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
from models.base import Base


class Rectangle(Base):
<<<<<<< HEAD
    """Represent a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.
        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
=======
    """
        class Rectangle implements Base.
        Methods:
            __init__()
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
            Initializes the instance of the class..
        """
        super().__init__(id)
>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
        self.width = width
        self.height = height
        self.x = x
        self.y = y
<<<<<<< HEAD
        super().__init__(id)

    @property
    def width(self):
        """Set/get the width of the Rectangle."""
=======

    @property
    def width(self):
        """
            getter function for __width
            Returns: width
        """
>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
        return self.__width

    @width.setter
    def width(self, value):
<<<<<<< HEAD
=======
        """
            setter function for width.
            Args:
                value (int): value to be set.
        """
>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
<<<<<<< HEAD
=======

>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
        self.__width = value

    @property
    def height(self):
<<<<<<< HEAD
        """Set/get the height of the Rectangle."""
=======
        """
            getter function for height
            Returns: height
        """
>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
        return self.__height

    @height.setter
    def height(self, value):
<<<<<<< HEAD
=======
        """
            setter function for height
            Args:
                value (int): value to be set.
        """
>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
<<<<<<< HEAD
=======

>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
        self.__height = value

    @property
    def x(self):
<<<<<<< HEAD
        """Set/get the x coordinate of the Rectangle."""
=======
        """
            getter function for x.
            Returns: x
        """
>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
        return self.__x

    @x.setter
    def x(self, value):
<<<<<<< HEAD
=======
        """
            setter function for x.
            Args:
                value (int): value to be set.
        """
>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
<<<<<<< HEAD
=======

>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
        self.__x = value

    @property
    def y(self):
<<<<<<< HEAD
        """Set/get the y coordinate of the Rectangle."""
=======
        """
            getter function for y
            Returns: y
        """
>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
        return self.__y

    @y.setter
    def y(self, value):
<<<<<<< HEAD
=======
        """
            setter function for y
            Args:
                value (int): value to be set.
        """
>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
<<<<<<< HEAD
        self.__y = value

    def area(self):
        """Return the area of the Rectangle."""
        return self.width * self.height

    def display(self):
        """Print the Rectangle using the `#` character."""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def update(self, *args, **kwargs):
        """Update the Rectangle.
        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return the print() and str() representation of the Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)
=======

        self.__y = value

    def area(self):
        """
            returns the area of the Rectangle instance.
        """
        return (self.__width * self.__height)

    def display(self):
        """
            prints to stdout the Rectangle instance with '#'
        """
        rectangle = ""
        print_symbol = "#"

#        for i in range(self.__height - 1):
#            rectangle += print_symbol * self.__width + "\n"
#        rectangle += print_symbol * self.__width

#        print("{}".format(rectangle))

        print("\n" * self.y, end="")

        for i in range(self.height):
            rectangle += (" " * self.x) + (print_symbol*self.width) + "\n"
        print(rectangle, end="")

    def __str__(self):
        """
            returns a string formart of the rectangle
        """
        return "[{}] ({}) {}/{} - {}/{}".format(type(self).__name__, self.id,
                                                self.__x, self.__y,
                                                self.__width, self.__height)

    def update(self, *args, **kwargs):
        """
            assigns key/value argument to attributes
            kwargs is skipped if args is not empty
            Args:
                *args -  variable number of no-keyword args
                **kwargs - variable number of keyworded args
        """
        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
            return

        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass

    def to_dictionary(self):
        """
            returns the dictionary repr of a rect
        """
        return {'x': getattr(self, "x"), 'y': getattr(self, "y"),
                'id': getattr(self, "id"), 'height': getattr(self, "height"),
                'width': getattr(self, "width")}
>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
