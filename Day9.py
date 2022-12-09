from ReadFile import ReadFile

filereader = ReadFile('InputFiles/InputDay9.txt', 'spaces')
input_lines = filereader.get_input()

head = {'x': 0, 'y':0}
tail = {'x': 0, 'y':0}
tail_visited = []

for line in input_lines:
    direction = line[0]
    steps = int(line[1])
    print(f'{direction}, {steps}')
    for i in range(1,steps+1):
        if direction == 'R':
            head['x'] += 1
            if not (head['x'] == tail['x'] + 1 and head['y'] == tail['y'])  and not (abs(head['x'] - tail['x'])==1 and abs(head['y'] - tail['y'])==1):
                tail['x'] +=1
        elif direction == 'L':
            head['x'] -= 1
            if not (head['x'] == tail['x'] - 1 and head['y'] == tail['y'])  and not (abs(head['x'] - tail['x'])==1 and abs(head['y'] - tail['y'])==1):
                tail['x'] -= 1
        elif direction == 'U':
            head['y'] += 1
            if not(head['y'] == tail['y'] + 1 and head['x'] == tail['x'])  and not (abs(head['x'] - tail['x'])==1 and abs(head['y'] - tail['y'])==1):
                tail['y'] += 1
        elif direction == 'D':
            head['y'] -= 1
            if (head['y'] == tail['y'] - 1 and head['x'] == tail['x'])  and not (abs(head['x'] - tail['x'])==1 and abs(head['y'] - tail['y'])==1):
                tail['y'] -= 1
        else:
            print(f'Direction {direction} unknown')
        if [tail['x'], tail['y']] not in tail_visited:
            tail_visited += [[tail['x'], tail['y']]]
        print(f'{tail["x"]}, {tail["y"]}')




print(f"Answer part 1 {len(tail_visited)}")