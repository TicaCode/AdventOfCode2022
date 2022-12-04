from ReadFile import ReadFile
from typing import List

file_reader = ReadFile('InputFiles/InputDay4.txt', '' , False)
input_lines = file_reader.get_input()

def find_overlap(input_lines: List):
    overlap = 0
    overlap_second = 0
    for line in input_lines:
        one, two = line.split(',')
        one = one.split('-')
        two = two.split('-')
        if (int(one[0]) >= int(two[0]) and int(one[1]) <= int(two[1])) or (int(one[0]) <= int(two[0]) and int(one[1])>=int(two[1])):
            overlap +=1
        elif (int(one[0]) <= int(two[1]) and int(two[0]) <= int(one[1])) or (int(two[0]) <= int(one[1]) and int(one[0]) <= int(two[1])):
            overlap_second += 1
    return overlap, overlap + overlap_second


answers = find_overlap(input_lines)
print(f'Answer part 1: {answers[0]}')
print(f'Answer part 2: {answers[1]}')