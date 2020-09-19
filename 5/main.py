import sys
import os
import math

# rm all files in output folder
def clear_output_folder(output_dir):
    os.system('rm {}/*'.format(output_dir))


# works only for dirs in current file's dir
def get_absolute_path(dirname_rel):
    return os.path.dirname(os.path.realpath(__file__)) + '/' + dirname_rel

# get all filenames from a dir
def get_input_filenames(dirname_abs):
    files = []
    for file in os.listdir(dirname_abs):
        temp_el = os.path.join(dirname_abs, file)
        if (os.path.isfile(temp_el)):
            files.append(temp_el)
    return files


# removes punctuation from lines and splits them by space
def get_words_from_line(line):
    punctuation = ', . /  : ; ? ! ( ) \n'.split(' ')
    for sign in punctuation:
        line = line.replace(sign, '')
    return line.lower().split(' ')


def remove_doubles(lst):
    lst = list(dict.fromkeys(lst))
    return lst    


# get all words from a file
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


def write_to_files(output_dir_abs, lst):
    longest_word = max(lst, key=len)
    for w in lst:
        if (w == ''):
            continue
        output_filename = output_dir_abs + '/' + w[0].upper() + '.txt'
        # test to print everything in one file
        output_filename = output_dir_abs + '/' + 'ALL' + '.txt'

        with open(output_filename, 'a') as outfile:
            spaces = ' ' * (len(longest_word) - len(w))
            temp_str = spaces + reverse(w) + '\n'
            outfile.write(temp_str)
    return True


def main():
    if (len(sys.argv) != 3):
        print("invalid number of arguments")
        sys.exit()

    
    # get absolute paths
    input_dir_abs = get_absolute_path(sys.argv[1])
    output_dir_abs = get_absolute_path(sys.argv[2])

    # create output folder of remove previous if exists
    if (not os.path.isdir(output_dir_abs)):
        # create folder if doesnt exist
        os.system('mkdir -p {}'.format(output_dir_abs))
        # os.mkdir(output_dir_abs)
    else:  
        clear_output_folder(output_dir_abs)


    input_filenames = get_input_filenames(input_dir_abs)

    all_words = []
    for f in input_filenames:
        all_words.extend(get_wordforms_from_file(f))

    # get wordforms w/o doubles
    all_words = remove_doubles(all_words)
    
    # flip to sort by ending
    all_words = flip_all_words(all_words)
    all_words.sort()

    # create dictionary
    write_to_files(output_dir_abs, all_words)

    print('ok')


if __name__ == '__main__':
    main()