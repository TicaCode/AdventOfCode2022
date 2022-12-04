from ReadFile import ReadFile
from typing import List

FileReader = ReadFile('InputFiles/InputDay3.txt', '', False)
input_lines = FileReader.get_input()

import string

alphabet = list(string.ascii_lowercase) + list(string.ascii_uppercase)
converter = {}
for i in range(52):
    converter[alphabet[i]] = i + 1


def get_double(string: str, converter: dict) -> int:
    first_half = string[0:int(len(string) / 2)]
    second_half = string[len(string) // 2:]
    not_found = True
    i = 0
    while not_found and i < len(string):
        if first_half[i] in second_half:
            output = converter[first_half[i]]
            return output
        else:
            i += 1
    return 0


def get_count(input_list: List, converter: dict):
    output = 0
    for i in input_list:
        output += get_double(i, converter)
    return output


print(f'Answer part 1: {get_count(input_lines, converter)}')


def get_double_from_list(input: List, converter: dict) -> int:
    first_half = input[0]
    second_half = input[1]
    third_half = input[2]
    not_found = True
    i = 0
    first_half = list(set(first_half))
    second_half = list(set(second_half))
    third_half = list(set(third_half))
    while not_found and i < len(first_half):
        if first_half[i] in second_half:
            print(first_half[i])
            if first_half[i] in third_half:
                not_found = False
                output = converter[first_half[i]]
                print(first_half[i])
                return output
            else:
                i += 1
        else:
            i += 1
    print('NOT FOUND!')
    return 0


def get_count_list(input_list: List, converter: dict):
    output = 0
    for i in range(0, len(input_list), 3):
        if i + 3 <= len(input_list):
            output += get_double_from_list(input_list[i:i + 3], converter)
    return output


print(f'Answer part 2: {get_count_list(input_lines, converter)}')
