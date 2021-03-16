# How to call parent class static method from child class static method by using super():

class A:

    @staticmethod
    def m1():
        print('Parent static method')

class B(A):
    @staticmethod
    def m2():
        super(B,B).m1()

B.m2()
