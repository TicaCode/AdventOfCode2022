from ReadFile import ReadFile
from typing import List

file_reader = ReadFile('InputFiles/InputDay5.txt', 'blank_lines')
input_lines = file_reader.get_input()

stack = input_lines[0]
moves = input_lines[1]

def read_stack(stack: List):
    stacks = {}
    piles = len(stack[len(stack)-1].split('   '))
    for i in range(1,piles+1):
        stacks[i] = [].copy()

    for line in stack[:-1]:
        index = 1
        for pile in range(1,piles+1):
            if index >= len(line):
                break
            if line[index] != ' ':
                stacks[pile].insert(0, line[index])
            index = index+4
    return stacks

def move(stacks: dict, instruction: str):
    parsed = instruction.split(' ')
    amount = int(parsed[1])
    from_pile = int(parsed[3])
    to_pile = int(parsed[5])
    for i in range(amount):
        move = stacks[from_pile].pop()
        stacks[to_pile] = stacks[to_pile] + [move]

def part_one(stack, moves):
    stacks = read_stack(stack)
    answer = ''
    for move_instr in moves:
        move(stacks, move_instr)
    for pile in stacks.keys():
        answer += (stacks[pile][-1])
    return answer

def move_multiple(stacks: dict, instruction: str):
    parsed = instruction.split(' ')
    amount = int(parsed[1])
    from_pile = int(parsed[3])
    to_pile = int(parsed[5])
    move = stacks[from_pile][-amount:]
    stacks[from_pile] = stacks[from_pile][:-amount]
    stacks[to_pile] = stacks[to_pile] + move

def part_two(stack, moves):
    stacks = read_stack(stack)
    answer = ''
    for move_instr in moves:
        move_multiple(stacks, move_instr)
    print(stacks)
    for pile in stacks.keys():
        answer += (stacks[pile][-1])

    return answer

print(f'Answer part 1: {part_one(stack, moves)}')
print(f'Answer part 2: {part_two(stack, moves)}')