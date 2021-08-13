from collections import defaultdict
from collections import OrderedDict
from collections import Counter
from collections import ChainMap
from collections import deque
from collections import namedtuple

'''Named tuple.
'''
# p = namedtuple('Course', ['x', 'y'])
# t = p('abhishek', 'python')
# t = p(11, y=22)
# j = t[0] + t[1]
# x, y = p     # UnPacking
# p.x + p.y


# EmployeeRecord = namedtuple('EmployeeRecord', 'name, age, title, department, paygrade')

# import csv
# for emp in map(EmployeeRecord._make, csv.reader(open("employees.csv", "rb"))):
#     print(emp.name, emp.title)

# import sqlite3
# conn = sqlite3.connect('/companydata')
# cursor = conn.cursor()
# cursor.execute('SELECT name, age, title, department, paygrade FROM employees')
# for emp in map(EmployeeRecord._make, cursor.fetchall()):
#     print(emp.name, emp.title)


# t = [11, 22]
# data = p._make(t)
# print(data)


# t = [11, 22]
# n = p._asdict(data)


# pd = p(x=11, y=22)
# print(pd._replace(x=33))


# dd = t(x=11, y=22)
# print(dd._replace(x=33))

# print(p._fields)
# getattr

# print(getattr(t, 'x'))


# Point = namedtuple('Point', 'x y')
# d = {'x': 11, 'y': 22}
# print(Point(**d))


"""Named Tuple.(use case for csv and database)
"""
point = namedtuple('Course', ['name', 'langueges'])
t = point('abhishek', 'python')
dic = t._asdict()  # convert into dictinary.

lst = [1, 2]

point_make = point._make(lst)

# print(point_make)
# print(dic)
# print(t)


"""deque
"""

a = ['r', '1', 'c', 'c', 'v', 'y']
a = deque(a)

a.append('python module')
a.appendleft('python module')
a.pop()
a.popleft()
# print(a)


"""ChainMap
"""

baseline = {'a': 'a1', 'b': 'b1'}
adjusments = {'c': 'c1', 'd': 'd1'}

cm = ChainMap(baseline, adjusments)
# print(dict(cm))


"""Counter
"""


a = [2, 3, 4, 5, 6, 7, 5, 2, 2, 2, 2, 2]

# print(Counter(a))
c = Counter(a)

# Element function
# print(list(c.elements()))

# most common
# print(list(c.most_common()))

# subtract function
s = {4: 2, 8: 3, 6: 1}
c.subtract(s)
# print(c)

"""OrderedDict.
"""

d = OrderedDict()

d[1] = 'r'
d[2] = 'i'
d[3] = 'c'

"""Default dict.
"""


# x = {1: 'Rifinder', 2: 'python', 3: 'collection'}
# print(x[4])

y = defaultdict(int)

y[1] = "cc"
y[2] = "ff"

print(y[3])

"""User dict ,User list, User string.
"""
