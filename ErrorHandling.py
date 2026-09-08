print(1)
print(2)
print(3)
print(4)
print(5)

# if True:
#     print(1)

# print("Hello"+9)
# print(0/4)
# print(5/0)

# try:
#     print("Step1")
#     print("Step2")
#     print("Step3")
#     print("Hello"+"55")
#     print(int("hello"))
#     print("Hi")
# except ValueError:
#     print("Invalid Conversion...!")
# except TypeError:
#     print("Invalid Expression")
# finally:
#     print("Done")

try:
    inp1=int(input("Entr your First Number: "))
    inp2=int(input("Entr your Sec Number: "))
    print(inp1/inp2)
except ValueError:
    print("Invalid Input..!")
except ZeroDivisionError:
    print("This number cannot be divided by 0!")

print(2)