# print(len(l1))
# print(l1[4])

# print(l1[3])

# l1[3]=0

# print(l1[3])

# l1.append(45)
# l1.append(455)
# l1.insert(-2,10) #10

# l1.extend(1)
# l1.extend("Hello")

# l1.remove(2)
# l1.remove(2)
# l1.pop(2)

# l1.pop()
# l1.pop()
# l1.pop()

# print(l1.index(4))
# print(l1.count(3))

# l1=[1,2,3,"Hello",3.14,True,2,3,4]
# l1.clear()
# print(l1)
# l1=[312,324,234,2134,2,2413,35,-1,0]
# l1.sort(reverse=True)
# print(l1)

# a="Hello world"

# print(a[10])

# a=[1,2,3,4,2,3,3,2,1,2,3,0]

# print(a[5]) #[4,5,4,3]
# print(a[-2:]) #[2,1]
# print(a[:3]) #[2,1] #0,1,2
# print(a[2:5])
# print(a[2:7:2]) #2,4,6
# print(a[::-1])

# print(a[2:3]) #[3]

# t1=(1,2,3,4,1,1,2,2)

# t1[6]=0

# print(t1.index(3))

# s1={1,2,3,4,5}
# s2={5,6,7,8}

# s1.add(100)
# s1.remove(52)
# s1.clear()

# print(s1.union(s2))
# print(s2.difference(s1))

# for i in {1,2,3}:
#     print(i)


# person1={
#     "name":"Ken",
#     "age":44,
#     "role":"FED",
#     "favMovies":[24,96,3],
#     "isMarried":True,
#     "isIndia":True,
#     # "name":"Hendry"
# }

# person1["age"]=45

# person1.pop("age")

# print(person1.keys()) 
# print(person1.values()) 
# print(person1.items()) 


# person=("Leo",23,"SASE")
# name=person[0]
# age=person[1]
# role=person[2]

# name,age,role=person

# print(role)
# a=1,2,3,4,5,6,7,8 #Tuple
# print(a)
# a,b=1,2
# print(b)

l1=[
    1,
    2,
    3,
    [
        "four",
        "five",
        [
            "six",
            "seven",
            "eight"
        ]
    ]
]

print(l1[-1][-1][-1][-1])