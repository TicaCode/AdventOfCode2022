from ReadFile import ReadFile

file_reader = ReadFile('InputFiles/InputDay6.txt', '')
input_line = file_reader.get_input()[0]

length_unique = 14
def find_first_unique(input_line: str, length_unique: int):
    found = False
    i = 0
    output = 0
    while found == False:
        string = input_line[i:i+length_unique]
        if len(set(string)) == length_unique:
            found = True
            output = i+ length_unique
        else:
            i +=1

    return output
print(f'Answer part 1: {find_first_unique(input_line, 4)}')
print(f'Answer part 2: {find_first_unique(input_line, 14)}')


