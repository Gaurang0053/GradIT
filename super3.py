class A:
    def __init__(self):
        print("A class Constructor")
    def m1(self):
        print('A class Method')
class B(A):
    def __init__(self):
        print("B class Constructor")
    def m1(self):
        print('B class Method')
class C(B):
    def __init__(self):
        print("C class Constructor")
    def m1(self):
        print('C class Method')
class D(C):
    def __init__(self):
        print("D class Constructor")
    def m1(self):
        print('D class Method')
class E(D):
    def __init__(self):
        print("E class Constructor")
    def m1(self):
        A.m1(self)
        super(D,self).m1()
        super(B,self).m1()
        super(B,self).__init__()

e=E()
e.m1()
