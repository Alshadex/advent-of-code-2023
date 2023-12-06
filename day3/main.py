import re

map_linetonums = {}

map_linetosymbols = {}

digits = re.compile(r'\d+')

def getAllIntegers(data: str, line_num: int) -> list[str]:
    map_linetonums[line_num] = []
    for match in re.finditer(digits, data):
        # print("line number:", line_num, "match", match.group(), "start index", match.start(), "End index", match.end())
        map_linetonums[line_num].append((match.group(), match.start(), match.end()))
    # return re.findall(digits, data)
    # print(data)
    # res = re.search(digits, data)
    # return res.span()

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
print(map_linetosymbols)


# for i in range(len(map_linetosymbols)):
#     for j in range(len(map_linetosymbols[i])):
#         print(map_linetosymbols[i][j][0], map_linetosymbols[i][j][1])


for i in range(1, 139):
    prev_line = map_linetonums[i-1]
    curr_line = map_linetonums[i]
    next_line = map_linetonums[i+1]
    # print(next_line)
    for symbol in map_linetosymbols[i]:
        # print(symbol)
        # pass 
        # print(symbol[0], symbol[1])