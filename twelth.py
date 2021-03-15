"""
class mit():
    def __init__(self):
        print("in const")

    def cs(self):
        print("cs")

m1=mit()
print(mit.__doc__)
m1.cs()

class mit():
    def __init__(self,a,b):
        self.a=10
        self.b=20

    def cs(self):
        print("cs")
m1=mit(10,20)
print(mit.__doc__)


class mit():
    def __init__(self ,a,b):
        self.a='grad'
        self.b=946

    def show (self):
        print(self.a,self.b)
m1 = mit('gradit',9455)
m1.show()

class mit():
    def __init__(self ,a,b):
        self.a='grad'
        self.b=946
        self.c='mit'

    def show (self):
        print(self.a,self.b,self.c)
m1 = mit('gradit',9455,)
m1.show()
print(mit.__doc__)
print(mit.__dict__)
print(help(mit))
"""
class mit():
    college="miot"
    def __init__(self):
        print(college)
    @classmethod
    def show(self):
        print(college)