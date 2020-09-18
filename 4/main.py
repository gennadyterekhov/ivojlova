import time
import random


MIN = 1
MAX = 10
MIN_LIST_LEN = 10
MAX_LIST_LEN = 100

# start timer
start_time = time.time()


def delete_all_ocurrences(lst, el):
    while (el in lst):
        lst.remove(el)
    return lst



element_to_delete = 5
list_to_check = [1, 2, 5, 4, 5, 5, 5, 6, 7, 5, 55, 8]


# list_to_check = random.sample(range(MIN, MAX + 1), MAX_LIST_LEN)
# element_to_delete = list_to_check[random.randint(MIN, MAX_LIST_LEN - 1)]


print("изначальный список (длина {}):".format(len(list_to_check)))
print(list_to_check)

# должно быть линейным
delete_all_ocurrences(list_to_check, element_to_delete)

print("список после обработки (длина {}):".format(len(list_to_check)))
print(list_to_check)


# print execution time
print("\nexecution time {} seconds".format(time.time() - start_time))