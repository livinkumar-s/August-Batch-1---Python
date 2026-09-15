class Parent:
    @staticmethod
    def greet():
        print("Hello")

# 1 method

class Child():
    @staticmethod
    def greet():
        print("Good morning")
    @staticmethod
    def sayHello():
        print("Hello")

# 2 meth

c1=Child()
p1=Parent()

c1.greet()
p1.greet()

# def add(a,b):
#     print(a+b)

# def add(a,b,c=0):
#     print(a+b+c)

# add(2,2)
# add(1,2,3)

# print(3+3) #add
# print("Hello"+"Hi") #concat