# is a relation method of inheritance
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eatndrink(self):
        print("eat biryani")

class employee(person):
    def __init__(self, name, age, eno, esal):
        super()__init_(name, age)
        self.eno = eno
        self.esal=esal

    def work(self):
        print()

    e=employee('gradit',48,100,1000)
    e.eatndrink()
    e.work()

