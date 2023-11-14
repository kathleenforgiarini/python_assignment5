"""
    Topic: Circle Class
    Date: 09 Nov 2023
    Author: Kathleen
"""

class Circle:
    __seq = 1

    def __init__(self, radius = 0.00, color="Red"):
        self.__circleId = f"CIR_{Circle.__seq}"
        self.__radius = radius
        self.__color = color
        Circle.__seq += 1

    def getCircleId(self):
        return self.__circleId
    
    def getRadius(self):
        return self.__radius
    
    def setRadius(self, radius):
        if radius < 0 or radius == None:
            print(f"{radius} - Radius can not be null or negative!")
        else:
            self.__radius = radius
    
    def getColor(self):
        return self.__color

    def setColor(self, color):
        if color == "" or color.isdigit() or color.isspace():
            print(f"{color} - Color can not be null or numerical!")
        else:
            self.__color = color

    def calculatePerimeter(self):
        return 2 * 3.1415 * self.__radius

    def calculateArea(self):
        return 3.1415 * self.__radius * self.__radius
    
    def __str__(self):
        return f"Circle Id: {self.__circleId}\tRadius: {self.__radius}\tColor: {self.__color}\tPerimeter: {self.calculatePerimeter()}\tArea: {self.calculateArea()}\n"

    def __del__(self):
        print(f"Circle {self.__circleId} has been deleted.")