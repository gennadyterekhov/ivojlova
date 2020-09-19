import matplotlib.pyplot as plt
import time


def plot(x, y):
    plt.plot(x, y)
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.title('Line graph!')
    plt.show()


def delete_all_ocurrences(lst, el):
    lst = [i for i in lst if i != el]
    return lst    


element_to_delete = 5
list_to_check = list(range(10))


x = []
y = []


lens = [x for x in range(1, 10000) if x % 100 == 0]
prev_time = 0.001
for test_list_len in lens:
    start_test_time = time.time()
    res = delete_all_ocurrences(list_to_check * test_list_len, element_to_delete)
    exec_time = time.time() - start_test_time
    growth = exec_time / prev_time
    prev_time = exec_time
    l = test_list_len * len(list_to_check)
    x.append(l)
    y.append(exec_time)
    print('готово (длина {})'.format(l))
    # print('готово (длина {}) время: {}\n дольше в {} раз чем предыдущая попытка'.format(l, exec_time, growth))

plot(x, y)