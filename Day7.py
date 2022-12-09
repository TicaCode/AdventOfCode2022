from ReadFile import ReadFile

file_reader = ReadFile('InputFiles/InputDay7.txt', 'spaces')
input_lines = file_reader.get_input()
directories = {}
path = ''

directories = {}
reading = False
for line in input_lines:
    if line[0] == '$' and line[1] == 'cd':
        if line[2] == '/':
            path = 'start'
            directories[path] = 0
        elif line[2] == '..':
            path = '/'.join(path.split('/')[0:-1])
        else:
            path = path +'/' + line[2]
        reading = False
    elif line[0] == '$' and line[1] == 'ls':
        reading = True
    else:
        if reading:
            if line[0] != 'dir':
                directories[path] += int(line[0])
            else:
                directories[path+ '/'+line[1]] = 0
total = 0
total_size = {}
for directory in directories.keys():
    contains = sum([directories[x]  for x in directories.keys() if directory in x])
    total_size[directory] = contains
    if contains <= 100000:
        total += contains

print(f'Answer part 1: {total}')

needed_space = 30000000
total_space = 70000000
used_space = total_size['start']
clear = (needed_space + used_space) - total_space
print(f'To clear: {clear}')
big_enough = [size for size in total_size.values() if size >= clear]
print(f'Answer part 2: {min(big_enough)}')
