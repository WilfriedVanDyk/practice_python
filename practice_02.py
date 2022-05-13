import copy
import datetime as dt

from dateutil import tz

# Time-zone-naive datetime object
timestamp = dt.datetime(2020, 1, 31, 14, 30)
print(timestamp.isoformat()) # '2020-01-31T14:30:00'

# Time-zone-aware datetime object
timestamp_eastern = dt.datetime(2020, 1, 31, 14, 30,
tzinfo=tz.gettz("Europe/Brussels"))
# Printing in isoformat makes it easy to see the offset from UTC
print(timestamp_eastern.isoformat()) # '2020-01-31T14:30:00-05:00'

"""
    Python 3.9 added proper time zone support to the standard library in the form of the
timezone module. Use it to replace the tz.gettz calls from dateutil:

from zoneinfo import ZoneInfo
timestamp_eastern = dt.datetime(2020, 1, 31, 14, 30,
tzinfo=ZoneInfo("US/Eastern"))
"""

# Assign a time zone to a naive datetime object
timestamp_eastern = timestamp.replace(tzinfo=tz.gettz("Europe/Brussels"))
print(timestamp_eastern.isoformat()) #'2020-01-31T14:30:00-05:00'

# Convert from one time zone to another.
# Since the UTC time zone is so common,
# there is a shortcut: tz.UTC
timestamp_utc = timestamp_eastern.astimezone(tz.UTC)
print(timestamp_utc.isoformat()) #'2020-01-31T19:30:00+00:00'

# From time-zone-aware to naive
timestamp_eastern.replace(tzinfo=None)
print(timestamp_eastern.isoformat())

# immutable or not?
a = [1, 2, 3]
b = a
print("a is assigned to b : assignment and immutable", a, b)
b[1] = 22
# print("change element of list b: assignment and immutable", a, b)

c = ((0,1), (2,3))
d = c
# creates erro: c[0] = (0,0)
# print(c,d)
# shallow copy
a = [1, 2, 3]
b = a.copy()
# a and b are [1, 2, 3]
a[1] = 22  # Changing "a"...
# a  => Out[25]: [1, 22, 3] BUT b => [1, 2, 3]  # shallow copy .copy()...doesn't affect "b"
# print("shallow copy but with immutable element: copy()", a, b)
# deep copy: what is the difference??
b = copy.deepcopy(a)
# print(a,b)
b[2] = 0
# print("deep copy", a, b)

# print("shallow immutable: copy.copy()")
list_a = [1, [2,3], 4]
list_b = copy.copy(list_a)
list_b[0] = 0
# print(list_a,list_b)


# print("deep mutable: copy.deepcopy()")
list_d = copy.deepcopy(list_a)
list_d[1][0] = 0
# print(list_a, list_d)

# print("shallow mutable")
list_c = copy.copy(list_a)
list_c[1][0] = 0
# print(list_a, list_c)

"""don't use an empty mutable parameter!!!
because the parameter is evaluated at the moment of the definition, not by calling the function!!
def add_one(x=[]):
    x.append(1)
    return x
 Do this:   
""" 
def add_one(x=None):
    if x is None:
        x = []
    x.append(1)
    return x

x = add_one()
add_one(x)
print("hi")
