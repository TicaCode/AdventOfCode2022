from ReadFile import ReadFile
from typing import List

FileReader = ReadFile('InputFiles/InputDay1.txt', 'blank_lines', True)
input_lines = FileReader.get_input()

totals = [sum(x) for x in input_lines]


def find_sum_max_n(totals: List, n: int) -> int:
    total_list = totals.copy()
    total_list.sort(reverse=True)
    return sum(total_list[0:n])


print(f'Answer part 1: {find_sum_max_n(totals, 1)}')
print(f'Answer part 2: {find_sum_max_n(totals, 3)}')
