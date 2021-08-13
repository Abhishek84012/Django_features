import webbrowser
from idlelib.debugger_r import debugging

# # Ternery operator
# condition = True
# x = 1 if condition else 0
# print(x)

# # Please use _ at big number.
# num1 = 1_0_0_000_00
# num2 = 10_00_0

# total = num1 + num2
# print(f"{total:,}")

# names = ["abhishek", "hemak"]

# for index, name in enumerate(names, start=1):
#     print(index, name)

# Both bind two list.
# names = ['peter', 'clark', 'wide']
# heros = ['spiderman', 'superman', 'pool']

# for index, name in enumerate(names):
#     hero = heros[index]
#     print(f'{name} is actually {hero}')

# use more than 2 list(len same hovi joye)
# for name, hero in zip(names, heros):
#     print(f'{name} is actually {hero}')

""" unpacking"""
# a, _ = (1, 2)
# print(a)
# # print(b)
# a,b,c =(1,2,3,4,5)
# a,*_ =(1,2,3,4,5)
# a,b,*c,d =(1,2,3,4,5)
# print(a)

"""class"""


# class Person():
#     pass


# person = Person()
# person.first ="first"
# print(person.first)

# setattr(person,'first','coray')
# first=getattr(person,'first')
# print(first)

# person_info = {'first': 'coray', 'last': 'schafer'}

# for key, value in person_info.items():
#     setattr(person, key, value)
# for key in person_info.keys():
#     print(getattr(person, key))

# on input you can use getpass() instead of input.(value not neccsray on get pass)
# x, y, z, p = input("Give me numbers: ").split()

# subs = 2400
# likes = 200
# comment = 56

# condions = [
#     subs > 150,
#     likes > 150,
#     comment > 50
# ]

# condions = [
#     subs > 150,
#     likes > 150,
#     comment > 50
# ]


# # OR condition
# if any(condions):
#     print("Awesome")

# # And condition
# if all(condions):
#     print("Awesome")

# Find Reapted most on list.
# most  =max(set(a),key=a.count)

# open link on web browser
# webbrowser.open("url", "url")

# Copy list
# deepcopy(list1)

# data = []
# print(locals())
# print("\n")
# print(globals())

# print('data' in locals(), 'data' in globals())

# def move_position(x,y,z):
#     print("")
# data = [10,2,30]
# move_position(*data)


output = []

# function used for removing nested
# lists in python.

