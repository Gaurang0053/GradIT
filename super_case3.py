# Case-3: From child class, class method we cannot access parent class instance methods and constructors by using super() directly(but indirectly possible). But we can access parent class static and class methods.
class P:
    def __init__(self):
        print('Parent Constructor')
    def m1(self):
        print('Parent instance method')
    @classmethod
    def m2(cls):
        print('Parent class method')
    @staticmethod
    def m3():
       print('Parent static method')

class C(P):
    @classmethod
    def m1(cls):
        # super().__init__()--->invalid
        # super().m1()--->invalid
        super().m2()
        super().m3()

C.m1()
