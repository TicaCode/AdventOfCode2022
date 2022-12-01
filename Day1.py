from ReadFile import ReadFile
from typing import List

FileReader = ReadFile('InputFiles/InputDay1.txt', 'blank_lines', True)
input_lines = FileReader.get_input()

totals = [sum(x) for x in input_lines]
print(f'Answer part 1: {max(totals)}')


def find_sum_max_n(totals: List, n: int) -> int:
    total_list = totals.copy()
    sum_max = 0
    for i in range(n):
        max_number = max(total_list)
        max_index = total_list.index(max_number)
        total_list = total_list[0:max_index] + total_list[max_index + 1:]
        sum_max += max_number
    return sum_max


print(f'Answer part 2: {find_sum_max_n(totals, 3)}')
