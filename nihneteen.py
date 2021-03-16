class A:
    def __init__(self):
        print("in constrctor")
    def __int__(self):
        print("in construcor 1")

    def sum(self,a,b):
        self.a=a
        self.b=b
        print(self.a+self.b)

    def sum(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        print(self.a+self.b+self.c)
a=A()
a.sum(10,30,20)

