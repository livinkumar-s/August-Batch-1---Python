# class Student:
#     def __init__(self,n,m):
#         self.name=n 
#         self.__mark=m #private

#     def getMarks(self):
#         print(self.__mark)


    

# class Child(Student):
#     def __init__(self, n, m): 
#         super().__init__(n, m)
#         self.grade="O"

# 2 attr + 1 attr

# s1=Student("Ken",76)
# c1=Child("Leo",99)

# print(s1.__mark)
# s1.getMarks()

class User:
    def __init__(self,u,p):
        self.username=u 
        self.__password=p
    def validateUser(self, enteredPass):
        if self.__password==enteredPass:
            return True 
        else:
            return False
    def changePass(self,curPass,newPass):
        if self.__password==curPass:
            self.__password=newPass
            print("Changed")
        else:
            print("Wrong Password")

class Child(User):
    def __init__(self, u, p):
        super().__init__(u, p)
    def printPass(self):
        print(super().__password)

# 2 meth 2 attr   
     
# u1=User("Leo","lepo123")
# print(u1.__password)
# print(u1.validateUser("lepo123"))
# u1.changePass("lepo123","79045")

# c1=Child("Leo","12345")

# print(c1.validateUser("123"))
# c1.printPass()