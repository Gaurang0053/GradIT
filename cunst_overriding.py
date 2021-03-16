class P:
    def __init__(self):
        print('Parent Constructor')

class C(P):
    def __init__(self):
        print('Child Constructor')
        
    def m1(self):
        print("child")

c=C()
