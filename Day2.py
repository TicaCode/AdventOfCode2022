from typing import List
from ReadFile import ReadFile

FileReader = ReadFile('InputFiles/InputDay2.txt', 'spaces', False)
input_lines = FileReader.get_input()
scores = {'X': 1, 'Y': 2, 'Z':3}

def calculate_win(battles: List, scores: dict):
    total_score = 0
    for battle in battles:
        opponent = battle[0]
        me = battle[1]
        if (opponent == 'A' and me == 'X') or (opponent == 'B' and me == 'Y') or (opponent == 'C' and me == 'Z'):
            total_score += scores[me] + 3
        elif (opponent == 'A' and me == 'Y') or (opponent == 'B' and me == 'Z') or (opponent == 'C' and me == 'X'):
            total_score += scores[me] + 6
        else:
            total_score += scores[me]
    return total_score

print(f'Answer part A: {calculate_win(input_lines, scores)}')


options = {'X': {'A':scores['Z'] , 'B':scores['X'] , 'C':scores['Y']},
            'Y': {'A': scores['X']+3,'B':scores['Y']+3 , "C": scores['Z']+3},
            'Z': {'A':scores['Y']+6, 'B':scores['Z']+6 , 'C':scores['X']+6 }}

def calculate_strategy(battles: List, options: dict):
    total_score = 0
    for battle in battles:
        total_score += options[battle[1]][battle[0]]
    return total_score

print(f'Answer part B: {calculate_strategy(input_lines, options)}')

