"""
    Topic: Book Class
    Date: 08 Nov 2023
    Author: Kathleen
"""

class Book:
    __seq = 0

    ### Constructor
    def __init__(self, bookTitle = "", bookAuthor = "", bookEditor = "", bookPrice = 0.00):

        self.__bookTitle = bookTitle 
        self.__bookAuthor = bookAuthor
        self.__bookEditor = bookEditor
        self.__bookPrice = bookPrice
        self.__bookId = Book.__seq
        Book.__seq += 1


    ### Instance Level Methods      

    def getBookTitle(self):
        return self.__bookTitle
    
    def getBookAuthor(self):
        return self.__bookAuthor
    
    def getBookEditor(self):
        return self.__bookEditor
    
    def getBookPrice(self):
        return self.__bookPrice
    
    def getBookId(self):
        return self.__bookId
    
    def setBookPrice(self, price):
        if price < 0 or price == None:
            print(f"{price} - Price can not be null or negative!")
        else:
            self.__bookPrice = price

    def __str__(self):
        return f"Book id: {self.__bookId}\tBook name: {self.__bookTitle}\tAuthor Name: {self.__bookAuthor}\tPrice: {self.__bookPrice}\n"
