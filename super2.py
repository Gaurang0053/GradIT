class P:
    a=10    #class variable
    def __init__(self):
        self.b=10   #instance variable

    def m1(self):
        print('Parent instance method')

    @classmethod        #decorator which describe that it is a class method
    def m2(cls):
        print('Parent class method')

    @staticmethod       #static method decorator
    def m3():
        print('Parent static method')

class C(P):
    a=888       #class variable
    def __init__(self):
        self.b=999
        super().__init__()
        print(super().a)
        super().m1()
        super().m2()
        super().m3()

c=C()
