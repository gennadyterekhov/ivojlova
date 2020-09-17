import math
import sys


# get digital representation of letter coordinate
def get_digit(ch):
    digits = [ 1, 2, 3, 4, 5, 6, 7, 8]
    letters = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    i = letters.index(ch)
    return digits[i]


# get distance between 2 points
def get_distance(point1, point2):
    a = abs(point1['x'] - point2['x'])
    b = abs(point1['y'] - point2['y'])
    return hypothenuse(a, b)


# calculate hypothenuse
def hypothenuse(a, b):
    return math.sqrt(a**2 + b**2)


# get field dict from str
def get_field(s):
    x1 = int(get_digit(s[0]))
    y1 = int(s[1])
    return {"x": x1, "y": y1}


if (len(sys.argv) != 3):
    print("invalid number of arguments")
    sys.exit()


# get fields: current field and field to check from input as strings
# field1_str = input("enter field 1>")
# field2_str = input("enter field 2>")
field1_str = sys.argv[1]
field2_str = sys.argv[2]

# convert from field str to point a1 to x:1 y:1
field1 = get_field(field1_str)
field2 = get_field(field2_str)

# sampe fields
a1 = get_field("a1")
b3 = get_field("b3")

# distance possible for knight to go
knight_distance = get_distance(a1, b3)
current_dictance = get_distance(field1, field2)
result = (current_dictance == knight_distance)
print(result)
