# from abc import ABC, abstractmethod

# #Abstract Class 
# class Animal(ABC):
#     @abstractmethod
#     def sound():
#         pass

# # a1=Animal()

# class Dog(Animal):
#     @staticmethod
#     def eat():
#         print("Dog is eating")

#     @staticmethod
#     def sound():
#         print("barking")

# class Cat(Animal):
#     @staticmethod
#     def eat():
#         print("Cat is eating")


# d1=Dog()
# d1.sound()

# c1=Cat()
# c1.eat()

from Payment import RazorPay,CashFree

r1=RazorPay()
c1=CashFree()

amount=int(input("Enter the amount: "))
c1.pay(1,amount)