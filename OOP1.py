class Bottle:
    brand="Aqua"
    def __init__(self,c,h,r):
        self.color=c
        self.height=h
        self.radius=r

    def sayVolume(self): #self=b2
        print((22/7)*(self.radius**2)*self.height)

    @classmethod
    def sayBrand(cls,a):
        print(a+cls.brand)

    @staticmethod
    def greet():
        print("Have a nice day")

    def __add__(self,other):
        return ((22/7)*(self.radius**2)*self.height)+((22/7)*(other.radius**2)*other.height)