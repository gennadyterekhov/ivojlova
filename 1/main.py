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
    x = int(get_digit(s[0]))
    y = int(s[1])
    return {"x": x, "y": y}


if (len(sys.argv) != 3):
    print("invalid number of arguments")
    sys.exit()


# get strings from arguments and convert to point ( example: a1 => {x:1,y:1} )
field_start = get_field(sys.argv[1])
field_finish = get_field(sys.argv[2])


# sample fields
a1 = get_field("a1")
b3 = get_field("b3")


# distance possible for knight to go
knight_distance = get_distance(a1, b3)

# distance between entered fields
current_distance = get_distance(field_start, field_finish)

# is distance the same
result = (current_distance == knight_distance)

print(result)
