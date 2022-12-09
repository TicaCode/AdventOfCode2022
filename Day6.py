from ReadFile import ReadFile

file_reader = ReadFile('InputFiles/InputDay6.txt', '')
input_string = file_reader.get_input()[0]


def find_first_unique(input_line: str, length_unique: int):
    found = False
    i = 0
    output = 0
    while not found:
        string = input_line[i:i+length_unique]
        if len(set(string)) == length_unique:
            found = True
            output = i+ length_unique
        else:
            i +=1

    return output


print(f'Answer part 1: {find_first_unique(input_string, 4)}')
print(f'Answer part 2: {find_first_unique(input_string, 14)}')


