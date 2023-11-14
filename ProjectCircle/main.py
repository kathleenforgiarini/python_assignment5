"""
    This is the main file
    Topic: Circle class
    Date: 09 Nov 2023
    Author: Kathleen
"""

from basisclasses.Circle import Circle

if __name__ == "__main__":
    c1 = Circle(3.0)
    c2 = Circle(4.2, "green")
    c3 = Circle(5.5, "yellow")

    print (c1)
    print (c2)
    print (c3)

    del (c1)
    del (c2)
    del (c3)
