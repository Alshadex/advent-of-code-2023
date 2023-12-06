import re
import copy

map_linetonums = {}

map_linetosymbols = {}

digits = re.compile(r'\d+')

def getAllIntegers(data: str, line_num: int) -> list[str]:
    map_linetonums[line_num] = []
    for match in re.finditer(digits, data):
        map_linetonums[line_num].append((match.group(), match.start(), match.end()))


def getAllSymbols(data: str, line_num: int) -> list[str]:
    map_linetosymbols[line_num] = []
    for i in range(len(data)):
        if not data[i].isdigit() and data[i] != ".":
            map_linetosymbols[line_num].append((data[i], i))



with open('input.txt', 'r') as file:
    data = file.read().split('\n')


line_num = 0
for i in data:
    getAllIntegers(i, line_num)
    getAllSymbols(i, line_num)
    line_num += 1
    
# print(map_linetonums)
# print(map_linetosymbols)
tmp_map_linetonums = copy.deepcopy(map_linetonums)

sum = 0
for i in range(1, 139):
    prev_line = map_linetonums[i-1]
    curr_line = map_linetonums[i]
    next_line = map_linetonums[i+1]

    print("line number: ", i)

    for symbol in map_linetosymbols[i]:
        print("     inspecting symbol: ", symbol[0], "at index: ", symbol[1])
        symbol_index = symbol[1]
        
        for integer in range(len(prev_line)):
            print("     inspecting integer prev_line: ", prev_line[integer][0])
            if symbol_index in range(prev_line[integer][1]-1, prev_line[integer][2]+1):
                print("         found int: ", prev_line[integer][0])
                sum += int(prev_line[integer][0])
                print("         sum: ", sum)
                tmp_map_linetonums[i-1].remove(prev_line[integer])
                
        for integer in range(len(curr_line)):
            print("     inspecting integer curr_line: ", curr_line[integer][0])
            if symbol_index in range(curr_line[integer][1]-1, curr_line[integer][2]+1):
                print("         found int: ", curr_line[integer][0])
                sum += int(curr_line[integer][0])
                print("         sum: ", sum)
                tmp_map_linetonums[i].remove(curr_line[integer])

        for integer in range(len(next_line)):
            print("     inspecting integer next_line: ", next_line[integer][0])
            if symbol_index in range(next_line[integer][1]-1, next_line[integer][2]+1):
                print("         found int: ", next_line[integer][0])
                sum += int(next_line[integer][0])
                print("         sum: ", sum)
                tmp_map_linetonums[i+1].remove(next_line[integer])

print(sum)