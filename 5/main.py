# 5. Зализняк. Дан путь к директории, в которой лежат текстовые файлы. Программа должна считать все тексты из этих файлов и все словоформы из этих текстов отсортировать по концу (как в словаре Зализняка). Словарь должен печататься в файлы "А.txt", "Б.txt", и так далее, в зависимости от последней буквы. Общий путь к этим файлам вводится с экрана, и может содержать несуществующие папки. Все файлы содержат много строк, и не должны ни в какой момент ни в каком виде целиком находиться в оперативной памяти. Сортировка должна учитывать букву ё. Программе для хранения совокупности словоформ разрешено использовать не более одного множества и не более одного списка (длины, соответствующей количеству различных словоформ в данных). Программа должна работать либо со сложностью, не превышающей сложность сортировки (быстрее, чем квадратично), либо не использовать множества (но тогда можно квадратично). Слова должны быть выровнены по правому краю, а ширина колонки должна зависеть от самого длинного встретившегося слова. 

TZ = '''
1. брать все файлы из папки инпут.
2. все их читать построчно
3. строки превращать в сет слов
4. и складывать в один большой лист
5. один большой лист в сет и обратно в лист чтобы удалить дубликаты
6. написать функцию сортировки по правому краю
7. пользователь может вводить путь до выходного файла, в т.ч не сущ. папки
'''


import sys
import os
# from os import listdir
# from os.path import isfile, join

INPUT_DIR = 'input'
OUTPUT_DIR = 'output'

def get_input_filenames(dirname):
    # в одну строку но я так не умею
    # onlyfiles = [f for f in os.listdir(input_dir) if os.path.isfile(os.path.join(input_dir, f))]

    # absolute path to input dir
    input_dir_abs = os.path.dirname(os.path.realpath(__file__)) + '/{}'.format(dirname)
    files = []
    for file in os.listdir(input_dir_abs):
        temp_el = os.path.join(input_dir_abs, file)
        if (os.path.isfile(temp_el)):
            files.append(temp_el)
    return files

# removes punctuation from lines and splits them by space
def get_words_from_line(line):
    punctuation = ', . /  : ; ? !'.split(' ')
    for sign in punctuation:
        line = line.replace(sign, '')
    return line.split(' ')


def remove_doubles(lst):
    lst = list(dict.fromkeys(lst))
    return lst    


def get_wordforms_from_file(filename):
    words = []
    with open(filename) as infile:
        for line in infile:
            words.extend(get_words_from_line(line))
    return words 


def reverse(s):
    return s[::-1]

def flip_all_words(lst):
    lst = list(map(reverse, lst))
    return lst


def write_to_file(filename):
    pass


def main():

    onlyfiles = get_input_filenames(INPUT_DIR)

    all_words = []
    for file in onlyfiles:
        all_words.extend(get_wordforms_from_file(file))

    # получаем словоформы без повторений
    all_words = remove_doubles(all_words)
    
    # отражаем чтобы отсортировать
    all_words = flip_all_words(all_words)
    all_words.sort()

    print(all_words)


if __name__ == '__main__':
    main()