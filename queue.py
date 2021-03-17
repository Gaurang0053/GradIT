class queue:
    def __init__(self):
        self.queue1 = []

    def push(self, val):
        l=len(self.queue1)
        if l<=10:
            print(self.queue1.append(val))
        else:
            print("overflow")

    def pop(self):
            self.queue1.pop(0)

    def printall(self):
        print(self.queue1)

    def isempty(self):
        return self.queue1 == []

q=queue()
while True:
    print("1.print")
    print("2.push")
    print("3.pop")
    print("4.exit")
    ch = int(input("enter ur choice"))

    if ch==1:
        q.printall()
    if ch==2:
        val=int(input("enter the value:"))
        q.push(val)
    if ch==3:
        q.pop()
    if ch==4:
        exit()










