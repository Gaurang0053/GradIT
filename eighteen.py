class Book:
    def __init__(self,pages):
        self.pages=pages

    def __int__(self,other):
        return self.pages+other.pages

b1=Book(100)
b2=Book(200)
print("the total no of pages",b1+b2)

