def get_digit(ch):
    digits = [ 1, 2, 3, 4, 5, 6, 7, 8]
    letters = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    i = letters.index(ch)
    return digits[i]

c = input()
print(get_digit(c))
