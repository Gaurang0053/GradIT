class a:
    def input1(self):
        self.x = int(input("Enter first number:"))

class b:
    def input2(self):
        self.y = int(input("Enter second number:"))


class c(a, b):
    def multiply(self):
        super().input1()
        super().input2()
        self.z = self.x * self.y
        print("multiplication  is:", self.z)

obj = c()
obj.multiply()