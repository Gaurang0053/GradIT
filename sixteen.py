class mob:
    """
    def __init__(self):
        print("in mob class")
    def features1(self):
        print("features1")
    def features2(self):
        print("features2")

class laptop(mob):
    def __init__(self):
        print("in laptop class")
    def features3(self):
        print("features3")
    def features4(self):
        print("features4")
"""

class a:
    def fec1(self):
        print("feature 1")
    def fec2(self):
        print("features2")

class b(a):
    def fec1(self):
        print("feature 1")

class c(b):
    def fec4(self):
        print("feature 4")

c1=c
c1.fec4
c1.fec3
c1.fec1










