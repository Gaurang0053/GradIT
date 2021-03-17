class stack:
    def __init__(self):
        self.stack1 = []

    def push(self, val):
        l=len(self.stack1)
        if l<=10:
            print(self.stack1.append(val))
        else:
            print("overflow")

    def pop(self):
            self.stack1.pop()

    def printall(self):
        print(self.stack1)

    def isempty(self):
        return self.stack1 == []

s=stack()
while True:
    print("1.print")
    print("2.push")
    print("3.pop")
    print("4.exit")
    ch = int(input("enter ur choice"))

    if ch==1:
        s.printall()
    if ch==2:
        val=int(input("enter the value:"))
        s.push(val)
    if ch==3:
        s.pop()
    if ch==4:
        exit()








