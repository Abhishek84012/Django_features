import itertools
from typing import Counter

'''Count function
'''
# counter = itertools.count()
# print(counter)
# for num in counter:
#     print(num)

# Ex.

# data = [100, 200, 300, 400]
# daily_data = zip(itertools.count(),data)

# print(daily_data)

# counter = itertools.count(start=5, step=5)

# for i in counter:
#     print(i)

# daily_data = list(zip((range(10)), data))
# print(daily_data)


'''Cycle
'''

# counter = itertools.cycle(("on","off"))
# print(counter)

# for i in counter:
#     print(i)
# counter = itertools.repeat(2,times=3)
# for i in counter:
#     print(i)

# squares = map(pow,range(10),itertools.repeat(3))
# print(list(squares))


letters = ['a', 'b', 'c', 'd']
numbers = [0, 1, 2, 3, 0, 8]
names = ["corey", "nicoles"]

data = letters + numbers + names

# print(data)

# result = itertools.combinations(names, 2)
# result1 = itertools.permutations(names, 2)
# result3 = itertools.product(numbers, repeat=5)
# result4 = itertools.combinations_with_replacement(numbers,5)

# print(list(result))
# print(list(result1))
# print(list(result3))
# print(list(result4))

# list concatination.
# combined = itertools.chain(letters, numbers, names)
# print(list(combined))

# combine = itertools.islice(range(10),2)
# combine = itertools.islice(letters,2,3)
# print(list(combine))
#
# selectors = [True,True,False,False,True]
# result = itertools.compress(letters,selectors)
# print(list(result))

# return false condition
result = itertools.filterfalse("function", numbers)
# return return false first time tyathi badhu lay le se.
result = itertools.dropwhile("function", numbers)
# false male ana pele nu badhu lese
result = itertools.takewhile("function", numbers)

# +
result = itertools.accumulate(numbers)
# print(list(result))


def get_state(person):
    return person['city']


people = [
    {
        'name': 'joe doe',
        'city': 'gothem'
    },
    {
        'name': 'joe doe',
        'city': 'gothem'
    },
    {
        'name': 'joe doe',
        'city': 'surat'
    }
]
# p = itertools.groupby(people, get_state)
# for key, g in p:
#     print(key)
#     for cc in g:
#         print(cc)

# copy1, copy2 = itertools.tee(people)
# print(list(copy2))
