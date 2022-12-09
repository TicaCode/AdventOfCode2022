from ReadFile import ReadFile

file_reader = ReadFile('InputFiles/InputDay8.txt', '')
input_lines = file_reader.get_input()

visible = 0
for index, line in enumerate(input_lines):
    for i in range(len(line)):
        if index == 0 or i == 0 or index == len(input_lines) -1 or i == len(line)-1:
            visible += 1
        else:
            horizontal_line = [int(x) for x in list(input_lines[index])]
            vertical_line = [int(temp_value[i]) for temp_value in input_lines]
            first_half_horizontal = horizontal_line[0:i]
            second_half_horizontal = horizontal_line[i+1:]
            first_half_vertical = vertical_line[0:index]
            second_half_vertical = vertical_line[index+1:]
            if max(first_half_horizontal) < int(horizontal_line[i]) or \
               max(second_half_horizontal) < int(horizontal_line[i]) or \
               max(first_half_vertical) < int(horizontal_line[i]) or \
               max(second_half_vertical) < int(horizontal_line[i]):
                visible += 1
                print(f'line {index}, index {i} visible')

print(f'Answer part 1: {visible}')

max_score = 0
visible = 0
for index, line in enumerate(input_lines):
    for i in range(len(line)):
        if index == 0 or i == 0 or index == len(input_lines) -1 or i == len(line)-1:
            score = 0
        else:
            horizontal_line = [int(x) for x in list(input_lines[index])]
            vertical_line = [int(temp_value[i]) for temp_value in input_lines]
            first_half_horizontal = horizontal_line[0:i]
            second_half_horizontal = horizontal_line[i+1:]
            first_half_vertical = vertical_line[0:index]
            second_half_vertical = vertical_line[index+1:]
            left = 0
            right = 0
            up = 0
            down = 0
            for temp_index in range(len(first_half_horizontal)):
                left += 1
                if first_half_horizontal[len(first_half_horizontal)-1-temp_index] >= horizontal_line[i]:
                    break

            for temp_index in range(len(second_half_horizontal)):
                right += 1
                if second_half_horizontal[temp_index] >= horizontal_line[i]:
                    break

            for temp_index in range(len(first_half_vertical)):
                up += 1
                if first_half_vertical[len(first_half_vertical) - 1 - temp_index] >= horizontal_line[i]:
                    break

            for temp_index in range(len(second_half_vertical)):
                down += 1
                if second_half_vertical[temp_index] >= horizontal_line[i]:
                    break

            score = left * right * up * down
            print(f'score {index} , {i}: {score}, {up}, {down}, {left}, {right}')
            if score > max_score:
                max_score = score

print(max_score)