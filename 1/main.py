# get digital representation of letter coordinate
def get_digit(ch):
    digits = [ 1, 2, 3, 4, 5, 6, 7, 8]
    letters = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    i = letters.index(ch)
    return digits[i]


# get all possible fields for a knight
def get_possible_fields(field)
    fields = []
    for i in range(1, 9):
        temp_x = field.x + 1
        temp_y = field.y + 2
    return [field, field]



# get fields: current field and field to check
field1_str = input("field 1")
field2 = input("field 2")

# set coordinates for field 1
x1 = get_digit(field1_str[0])
y1 = field1_str[1]

# set coordinates for field 2
x2 = get_digit(field2_str[0])
y2 = field2_str[1]


field1 = {
    "x": x1,
    "y": y1
}


field2 = {
    "x": x2,
    "y": y2
}


result = (field2 in get_possible_fields(field1))
print(result)

