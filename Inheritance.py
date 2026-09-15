class Calc:
    version="0.0.0.0"
    @staticmethod
    def addNum(a,b):
        print(a+b)
    @staticmethod
    def subNum(a,b):
        print(a-b)

#2 meth

class AdvCal(Calc):
    version="1.0.0.0"
    @staticmethod
    def mulNum(a,b):
        print(a*b)
    @staticmethod
    def divNum(a,b):
        print(a/b)

#4 meth

class SciCalc(Calc):
    version="2.0.0.0"
    @staticmethod
    def floorDiv(a,b):
        print(a//b)

#3 meth

c1=Calc()
c2=AdvCal()
c3=SciCalc()

c3.addNum(99,1)