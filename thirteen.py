class test:
    a=10
    def __init__(self):
        print(self.a)#instance variable
        print(test.a) #class variable

    def m1(self):
        print(self.a) #instance variable
        print(test.a) #class variable
    @classmethod

    def m2(cls): #class method
        print(cls.a) #class variable
        print(test.a)
    @staticmethod
    def m3():
        print(test.a)
t=test()
print(test.a)
print(t.a)

t.m1()
t.m2()
t.m3()